import flet as ft

class CustomColumn(ft.UserControl):
    """
    Clase personalizada para orginzar elementos en columna.
    """
    def __init__(self, controls = None, spacing:int= 10 ):
        super().__init__()
        self.controls = controls if controls else []
        self.spacing = spacing
        #self.alignment = alignment if isinstance(alignment, ft.MainAxisAlignment) else ft.MainAxisAlignment.START

        self.column = None # Referencia interna a la columna

    def build(self):
        """
        Construye la columna con los parametros definidos..
        """
        self.column =  ft.Column(
            controls=self.controls,
            spacing=self.spacing,
            alignment=self.alignment
        )
        return self.column # Ahora `build()` devuelve la columna almacenada en `self.column`

    def add_control(self, control):
            """
            Agrega un nuevo control a la columna sin necesidad de reconstruir todo el UserControl.
            """
            #agregamos validacion
            if self.column:
                self.column.controls.append(control)
                self.column.update()  # Solo actualiza la columna sin reconstruir todo el control


    def remove_control(self, control):
        """
        Elimina un control de la columna si existe.
        """
        if self.column and control in self.column.controls:
            self.column.controls.remove(control)
            self.column.update()  # Actualiza solo la columna

    def clear_controls(self):
        """
        Elimina todos los controles de la columna.
        """
        if self.column: # validamos de que self.columns no sea None

            self.column.controls.clear()
            self.column.update()


if __name__ == "__main__":

    def main(page: ft.Page):
        page.title = "Ejemplo de CustomColumn con referencia interna"

        # ✅ Crear una columna vacía
        columna = CustomColumn()
        
        # ✅ Botón para agregar elementos a la columna
        def add_element(e):
            columna.add_control(ft.Text("Nuevo elemento agregado"))

        # ✅ Botón para limpiar la columna
        def clear_elements(e):
            columna.clear_controls()

        btn_add = ft.ElevatedButton("Agregar elemento", on_click=add_element)
        btn_clear = ft.ElevatedButton("Limpiar columna", on_click=clear_elements)

        page.add(btn_add, btn_clear, columna)

    ft.app(target=main)