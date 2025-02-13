import flet as ft
from devices.esp32_device import Esp32Device
from utils.mqtt_manager import MQTTManager
from utils.data_manager import save_devices, load_devices

class AdministrarESP32Tab(ft.Column):
    def __init__(self, mqtt_manager: MQTTManager):
        super().__init__()
        self.mqtt_manager = mqtt_manager
        self.devices = {}  # Diccionario para almacenar dispositivos ESP32

        # Inicializamos los elementos de la UI
        self.device_input = ft.TextField(label="ID del Dispositivo", on_submit=self.add_device)
        self.devices_list = ft.Column()  # Lista de dispositivos

        # Construimos la UI
        self.controls = [self.build_ui()]

    def build_ui(self):
        """Construye la interfaz de administración de dispositivos"""
        return ft.Column([
            ft.Text("Administrar ESP32", size=30, weight=ft.FontWeight.BOLD),
            ft.Row([
                self.device_input,  # Usamos la variable directamente
                ft.ElevatedButton(text="Agregar Dispositivo", on_click=self.add_device)
            ]),
            self.devices_list  # Agregamos la lista de dispositivos
        ])

    def add_device(self, e):
        """Añadir un nuevo dispositivo ESP32 a la lista"""
        device_id = self.device_input.value.strip()
        if not device_id or device_id in self.devices:
            return  # Evitar dispositivos duplicados o vacíos

        device = Esp32Device(device_id)
        self.devices[device_id] = device
        self.devices_list.controls.append(device)
        self.devices_list.update()

        # Guardar el estado en la base de datos
        save_devices(self.devices)

    def load_existing_devices(self, e=None):
        """Cargar dispositivos desde la base de datos después de que la UI esté lista"""
        existing_devices = load_devices()
        for device_id in existing_devices:
            device = Esp32Device(device_id)
            self.devices[device_id] = device
            self.devices_list.controls.append(device)  # Agregar a la UI
        
        # Actualizar la UI solo después de que la página esté lista
        if self.page:
            self.devices_list.update()
