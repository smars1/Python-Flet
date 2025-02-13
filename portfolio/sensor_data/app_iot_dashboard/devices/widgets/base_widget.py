import flet as ft

class BaseWidget(ft.Row):
    def __init__(self, name, key):
        super().__init__()
        self.name = name
        self.key = key
        self.value = "--"
        self.build_ui()

    def build_ui(self):
        """Interfaz común de los widgets"""
        self.controls = [
            ft.Text(f"{self.name}: {self.value}", size=14),
            ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e: self.delete_widget()),
            ft.IconButton(icon=ft.icons.UPDATE, on_click=lambda e: self.update_widget())
        ]

    def update_widget(self):
        """Actualizar el widget (lógica personalizada en cada tipo de widget)"""
        pass

    def delete_widget(self):
        """Eliminar el widget"""
        self.controls.clear()
        self.update()
