import flet as ft
from utils.mqtt_manager import MQTTManager
class VisualizarDatosTab(ft.Column):
     def __init__(self, mqtt_manager: MQTTManager):
        super().__init__()
        self.mqtt_manager = mqtt_manager  # Almacenar la instancia de MQTT
        self.controls = [
            ft.Text("Visualizar Datos", size=30, weight=ft.FontWeight.BOLD),
            ft.Text("Aquí puedes visualizar datos."),
        ]