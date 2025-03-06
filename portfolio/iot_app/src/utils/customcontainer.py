import flet as ft

class CustomContainer(ft.UserControl):
    """
    Contenedor personalizado para estructurar visualmente los componentes.
    """

    def __init__(self, content=None, width=400, height=400, padding=20, bgcolor=ft.colors.BLUE_GREY_50, border_radius=10, alignment=ft.alignment.center):
        super().__init__()
        self.content = content if content else ft.Column()  #  Si no hay contenido, asignamos un `Column` vacío
        self.width = width
        self.height = height
        self.padding = padding
        self.bgcolor = bgcolor
        self.border_radius = border_radius
        self.alignment = alignment

    def build(self):
        """
        Construye el `Container` con los parámetros dados.
        """
        self.container = ft.Container(
            content=self.content,  
            width=self.width,
            height=self.height,
            padding=self.padding,
            bgcolor=self.bgcolor,
            border_radius=self.border_radius,
            alignment=self.alignment  #  Aseguramos alineación
        )
        return self.container  

    def update_content(self, new_content):
        """
        Permite actualizar el contenido dinámicamente.
        """
        if self.container:
            self.container.content = new_content  #  Actualizamos el contenido
            self.container.update()  #  Refrescamos la UI
            self.update()  #  Refrescamos `UserControl`


if __name__ == "__main__":
    #container = CustomContainer()
    #ft.app(target=container)  #  Ejecutamos la aplicación con el contenedor personalizado
    from customcolumn import CustomColumn   
    from custombutton import CustomButton
    def main(page: ft.Page):
        page.title = "Prueba de CustomContainer"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER  #  Centramos todo

        #  Creamos una columna personalizada
        custom_column = CustomColumn()

        #  Creamos botones para modificar la columna
        btn_add = CustomButton("Agregar", on_click=custom_column.add_element, bgcolor=ft.colors.GREEN_500)


        #  Creamos un contenedor con la columna y el botón dentro
        custom_container = CustomContainer(
            content=ft.Column([btn_add, custom_column]),  # 📌 Se agregan elementos visibles
            width=500,
            height=500,
            bgcolor=ft.colors.WHITE,
            padding=30,
            border_radius=15
        )
        container = CustomContainer(bgcolor=ft.colors.ORANGE_50)

        page.add(custom_container, container)  

    ft.app(target=main)
