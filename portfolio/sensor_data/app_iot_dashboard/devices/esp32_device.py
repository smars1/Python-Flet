import flet as ft
from devices.widgets.base_widget import BaseWidget

class Esp32Device(ft.Column):
    def __init__(self, device_id):
        super().__init__()
        self.device_id = device_id
        self.widgets = []
        self.controls = [self.build_device_ui()]

    def add_widget(self, widget):
        """Agregar un widget al ESP32"""
        self.widgets.append(widget)
        self.controls.append(widget)
        self.update()

    def remove_widget(self, widget):
        """Eliminar un widget del ESP32"""
        if widget in self.widgets:
            self.widgets.remove(widget)
            self.controls.remove(widget)
            self.update()


    def build_device_ui(self):
        """Construir la interfaz de un dispositivo"""
        return ft.Row([
            ft.Text(f"Dispositivo: {self.device_id}", size=16, weight=ft.FontWeight.BOLD),
            ft.IconButton(icon=ft.icons.DELETE, on_click=self.remove_device)
        ])

    def remove_device(self, e):
        """Eliminar este dispositivo de la lista"""
        self.controls.clear()
        self.update()
