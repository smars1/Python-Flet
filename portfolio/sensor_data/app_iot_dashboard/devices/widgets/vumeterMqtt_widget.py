from devices.widgets.base_widget import BaseWidget
import flet as ft
from utils.mqtt_manager import mqtt_manager

class VUMeterWidget(BaseWidget):
    def __init__(self, name, key):
        super().__init__(name, key)
        self.bar = ft.ProgressBar(value=0.0)
        self.controls.append(self.bar)

        # Suscribirse a un tópico específico de datos del ESP32
        mqtt_manager.client.message_callback_add(f"iot/{self.key}", self.on_mqtt_message)
        
    def on_mqtt_message(self, client, userdata, message):
        """Actualizar la barra de progreso con los datos recibidos"""
        try:
            new_value = float(message.payload.decode())
            self.bar.value = min(1.0, max(0.0, new_value))
            self.update()
        except ValueError:
            print("Error en la conversión del valor recibido")
