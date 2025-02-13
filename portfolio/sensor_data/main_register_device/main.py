import flet as ft
import requests
import json
import os
from config import AWS_API_URL, AWS_API_KEY

# 🔹 Definir la ubicación del archivo de configuración y datos
CONFIG_DIR = os.path.join(os.getenv("APPDATA") or os.path.expanduser("~/.config"), "IOT_Dashboard")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
DATA_FILE = os.path.join(CONFIG_DIR, "devices_data.json")

# 🔹 Asegurar que la carpeta de configuración exista
os.makedirs(CONFIG_DIR, exist_ok=True)

# 🔹 Función para cargar la configuración
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    return {
        "API_URL": AWS_API_URL,
        "API_KEY": AWS_API_KEY
    }

# 🔹 Función para guardar la configuración
def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

# 🔹 Cargar configuración al inicio
config = load_config()
API_URL = config["API_URL"]
API_KEY = config["API_KEY"]

# 🔹 Función para cargar dispositivos desde el archivo
def load_devices():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)

            if not isinstance(data, dict):
                return {}

            for device_id in data:
                if not isinstance(data[device_id], dict) or "widgets" not in data[device_id]:
                    data[device_id] = {"widgets": []}

            return data
        return {}
    except (json.JSONDecodeError, ValueError) as e:
        print(f"❌ Error al cargar dispositivos: {e}")
        return {}

# 🔹 Función para guardar dispositivos en archivo JSON
def save_devices(devices):
    try:
        serializable_data = {
            device_id: {"widgets": device.widgets} for device_id, device in devices.items()
        }
        with open(DATA_FILE, "w") as f:
            json.dump(serializable_data, f, indent=4)
        print(f"✅ Dispositivos guardados correctamente en {DATA_FILE}")
    except Exception as e:
        print(f"❌ Error al guardar dispositivos: {e}")

# 🔹 Clase para representar un dispositivo ESP32
class Esp32Device(ft.Column):
    def __init__(self, device_id, remove_device_callback, widgets=None):
        super().__init__()
        self.device_id = device_id
        self.widgets = widgets if widgets else []
        self.remove_device_callback = remove_device_callback
        self.show_delete = True  
        self.show_update = True  
        self.controls = [self.build_device_ui()]
    
    def fetch_data(self):
        headers = {"x-api-key": API_KEY}
        response = requests.get(f"{API_URL}?device_id={self.device_id}", headers=headers)
        if response.status_code == 200:
            return response.json()
        return {}

    def update_widgets(self):
        data = self.fetch_data()
        for widget in self.widgets:
            widget["value"] = data.get(widget["key"], "--")
        self.controls = [self.build_device_ui()]
        self.update()
        save_devices(dispositivos)

    def add_widget(self, widget_type, key, widget_name):
        new_widget = {
            "type": widget_type,
            "key": key,
            "name": widget_name,
            "value": "--",
            "editing": False
        }
        self.widgets.append(new_widget)
        self.update_widgets()

    def remove_widget(self, widget):
        self.widgets.remove(widget)
        self.update_widgets()

    def build_device_ui(self):
        widget_elements = []
        for widget in self.widgets:
            widget_elements.append(ft.Row([
                ft.Text(f"{widget['name']}: {widget['value']}", size=14),
                ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, w=widget: self.remove_widget(w), visible=self.show_delete),
                ft.IconButton(icon=ft.icons.UPDATE, on_click=lambda e: self.update_widgets(), visible=self.show_update)
            ]))
        return ft.Column([
            ft.Row([
                ft.Text(f"Dispositivo: {self.device_id}", size=16, weight=ft.FontWeight.BOLD),
                ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e: self.remove_device_callback(self.device_id), visible=self.show_delete)
            ]),
            ft.Column(widget_elements, spacing=10)
        ], spacing=10)

# 🔹 Función principal de la app
def main(page: ft.Page):
    page.title = "ESP32 IoT Dashboard"
    page.scroll = "auto"
    global dispositivos
    dispositivos = {}
    stored_devices = load_devices()
    
    def actualizar_dispositivos():
        dispositivo_selector.options = [ft.dropdown.Option(dev_id) for dev_id in dispositivos]
        dispositivo_selector.update()
        page.update()
    
    def agregar_dispositivo(e):
        dispositivo = dispositivo_input.value.strip()
        if dispositivo and dispositivo not in dispositivos:
            device = Esp32Device(dispositivo, remove_dispositivo)
            dispositivos[dispositivo] = device
            pestañas[1].content.controls.append(device)
            save_devices(dispositivos)
            actualizar_dispositivos()
            page.update()
    
    def agregar_widget(e):
        device_id = dispositivo_selector.value
        widget_type = widget_selector.value
        key = clave_input.value.strip()
        widget_name = nombre_widget_input.value.strip()
        
        if device_id in dispositivos and widget_type and key and widget_name:
            dispositivos[device_id].add_widget(widget_type, key, widget_name)
            save_devices(dispositivos)
            page.update()
    
    def remove_dispositivo(device_id):
        if device_id in dispositivos:
            device = dispositivos.pop(device_id)
            pestañas[1].content.controls.remove(device)
            save_devices(dispositivos)
            actualizar_dispositivos()
            page.update()
    
    # 📌 Configuración
    api_url_input = ft.TextField(value=config["API_URL"], label="API URL", expand=True)
    api_key_input = ft.TextField(value=config["API_KEY"], label="API KEY", expand=True, password=True)

    def guardar_config(e):
        config["API_URL"] = api_url_input.value
        config["API_KEY"] = api_key_input.value
        save_config(config)
        page.snack_bar = ft.SnackBar(ft.Text("Configuración guardada correctamente"), bgcolor=ft.colors.GREEN)
        page.snack_bar.open = True
        page.update()

    btn_guardar_config = ft.ElevatedButton("Guardar Configuración", on_click=guardar_config)

    # 📌 Crear UI
    dispositivo_input = ft.TextField(label="ID del ESP32", expand=True)
    btn_agregar = ft.ElevatedButton("Agregar Dispositivo", on_click=agregar_dispositivo)
    dispositivo_selector = ft.Dropdown(label="Seleccionar Dispositivo", options=[])
    widget_selector = ft.Dropdown(
        options=[ft.dropdown.Option("barras"), ft.dropdown.Option("progreso"), ft.dropdown.Option("texto"), ft.dropdown.Option("boton")], 
        label="Seleccionar Widget"
    )
    clave_input = ft.TextField(label="Clave JSON", expand=True)
    nombre_widget_input = ft.TextField(label="Nombre del Widget", expand=True)
    btn_widget = ft.ElevatedButton("Agregar Widget", on_click=agregar_widget)

    pestañas = [
        ft.Tab(text="Administrar ESP32", content=ft.Column([
            ft.Row([dispositivo_input, btn_agregar], spacing=10),
            ft.Row([dispositivo_selector, widget_selector, clave_input, nombre_widget_input, btn_widget], spacing=10),
        ], spacing=20)),
        ft.Tab(text="Visualizar Datos", content=ft.Column([], spacing=20, scroll="adaptive")),
        ft.Tab(text="Configuración", content=ft.Column([
            api_url_input,
            api_key_input,
            btn_guardar_config
        ], spacing=10)),
    ]
    
    tab_view = ft.Tabs(tabs=pestañas, expand=1)
    page.add(tab_view)

    for dev_id, data in stored_devices.items():
        device = Esp32Device(dev_id, remove_dispositivo, widgets=data.get("widgets", []))
        dispositivos[dev_id] = device
        pestañas[1].content.controls.append(device)

    actualizar_dispositivos()
    page.update()

ft.app(target=main)
