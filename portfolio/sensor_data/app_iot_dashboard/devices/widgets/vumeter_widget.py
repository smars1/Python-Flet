from devices.widgets.base_widget import BaseWidget
import flet as ft
import boto3
import time
import threading

class VUMeterWidget(BaseWidget):
    def __init__(self, name, key, table_name):
        super().__init__(name, key)
        self.bar = ft.ProgressBar(value=0.0)
        self.controls.append(self.bar)
        self.table_name = table_name
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table(self.table_name)
        
        # Iniciar un hilo para actualizar el valor cada 5 segundos
        self.update_thread = threading.Thread(target=self.update_widget)
        self.update_thread.daemon = True
        self.update_thread.start()

    def update_widget(self):
        """Obtener datos desde DynamoDB y actualizar la barra"""
        while True:
            response = self.table.get_item(Key={"device_id": self.key})
            if "Item" in response:
                new_value = float(response["Item"].get("sensor_value", 0.0))
                self.bar.value = min(1.0, max(0.0, new_value))
                self.update()
            time.sleep(5)  # Actualizar cada 5 segundos
