import flet as ft

class CustomRow(ft.UserControl):
    """
    Clase personalizada para organizar elementos en una fila con referencia interna.
    """

    def __init__(self, controls=None, spacing=10, alignment=None):
        super().__init__()
        self.controls = controls if controls else []
        self.spacing = spacing
        self.alignment = alignment
        self.row = None  # 🔹 Referencia interna a la fila

    def build(self):
        """
        Construye la fila y guarda la referencia.
        """
        self.row = ft.Row(
            controls=self.controls,
            spacing=self.spacing,
            alignment=self.alignment
        )
        return self.row  # 🔹 Retornamos la fila guardada en `self.row`

    def add_control(self, control):
        """
        Agrega un nuevo control a la fila.
        """
        self.row.controls.append(control)
        self.row.update()  # 🔹 Solo actualiza la fila

    def remove_control(self, control):
        """
        Elimina un control de la fila si existe.
        """
        if control in self.row.controls:
            self.row.controls.remove(control)
            self.row.update()

    def clear_controls(self):
        """
        Elimina todos los controles de la fila.
        """
        self.row.controls.clear()
        self.row.update()


if __name__ == "__main__":
    def main(page: ft.Page):
        page.title = "Ejemplo de CustomRow con referencia interna"

        # Crear una fila vacía
        fila = CustomRow()

        # Botón para agregar elementos a la fila
        def add_element(e):
            fila.add_control(ft.Text("Nuevo elemento agregado"))

        # Botón para limpiar la fila
        def clear_elements(e):
            fila.clear_controls()

        btn_add = ft.ElevatedButton("Agregar elemento", on_click=add_element)
        btn_clear = ft.ElevatedButton("Limpiar fila", on_click=clear_elements)

        page.add(btn_add, btn_clear, fila)

    ft.app(target=main)

