import flet as ft
from utils.custombutton import CustomButton
from utils.customcolumn import CustomColumn
from utils.customcontainer import CustomContainer

class MainView(ft.UserControl):
    """
    Clase principal que integra `CustomButton`, `CustomColumn` y `CustomContainer`.
    """

    def __init__(self):
        super().__init__()
        self.custom_column = CustomColumn()  # ✅ Instancia de `CustomColumn`
        self.custom_container = None # 🔹 Referencia al `CustomContainer`

    def build(self):
        """
        Construye la interfaz principal con botones y la columna dentro de `CustomContainer`.
        """
        btn_add = CustomButton("Agregar", on_click=self.custom_column.add_element, bgcolor=ft.colors.GREEN_500)
        btn_remove = CustomButton("Eliminar último", on_click=self.custom_column.remove_element, bgcolor=ft.colors.RED_500)
        btn_clear = CustomButton("Limpiar columna", on_click=self.custom_column.clear_elements, bgcolor=ft.colors.ORANGE_500)

        # ✅ Aseguramos que `CustomContainer` contenga una estructura válida
        content = ft.Column(
            controls=[
                btn_add,
                btn_remove,
                btn_clear,
                self.custom_column  # ✅ Ahora `CustomColumn` está bien referenciado
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        self.custom_container = CustomContainer(content=content, width=500, height=500)  # ✅ Se usa `CustomContainer`

        return ft.Column(  # 🔹 Retornamos una estructura con un `Column`
            controls=[self.custom_container], 
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def update_container(self):
        """
        Método para forzar la actualización del contenedor.
        """
        if self.custom_container:
            self.custom_container.update_content(self.custom_column)  # 🔹 Se actualiza el contenido dinámicamente

if __name__== "__main__":

    def main(page: ft.Page):
        page.title = "Prueba de CustomContainer"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER  #  Centramos todo

        #  Creamos una columna personalizada
        view = MainView()

        page.add(view)  

    ft.app(target=main)