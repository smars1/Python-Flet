from devices.widgets.base_widget import BaseWidget
import flet as ft
from utils.mqtt_manager import mqtt_manager  # Importamos la instancia global

class ButtonWidget(BaseWidget):
    def __init__(self, name, key):
        super().__init__(name, key)
        self.button = ft.ElevatedButton(text=self.name, on_click=self.toggle_state)
        self.controls.append(self.button)
        self.state = False

    def toggle_state(self, e):
        """Cambiar estado y publicar en MQTT"""
        self.state = not self.state
        self.button.text = "Encendido" if self.state else "Apagado"

        # Publicar en MQTT
        mqtt_manager.publish("iot/button", str(self.state))
        
        self.update()
