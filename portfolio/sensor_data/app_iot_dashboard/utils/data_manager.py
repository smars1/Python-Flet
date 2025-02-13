import json
import os

CONFIG_PATH = os.path.expanduser("~/.config/iot_dashboard")
DEVICES_FILE = os.path.join(CONFIG_PATH, "devices_data.json")

def ensure_config_dir():
    """Asegurar que la carpeta de configuración existe"""
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(CONFIG_PATH)

def save_devices(dispositivos):
    """Guardar los dispositivos en un archivo JSON"""
    ensure_config_dir()
    data = {dev.device_id: [w.__class__.__name__ for w in dev.widgets] for dev in dispositivos.values()}
    with open(DEVICES_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_devices():
    """Cargar los dispositivos desde el archivo JSON"""
    if os.path.exists(DEVICES_FILE):
        with open(DEVICES_FILE, "r") as f:
            return json.load(f)
    return {}
