import flet as ft

class ConfiguracionTab(ft.Column):
    def __init__(self):
        super().__init__()
        self.controls = [
            ft.Text("Configuración", size=30, weight=ft.FontWeight.BOLD),
            ft.Text("Aquí puedes configurar tus credenciales."),
        ]