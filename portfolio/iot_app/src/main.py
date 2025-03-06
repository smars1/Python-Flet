import flet as ft
from views.mainview import MainView

def main(page: ft.Page):
    page.title = "Aplicación con CustomContainer"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # ✅ Centramos todo

    # ✅ Creamos una instancia de la vista principal
    main_view = MainView()

    # ✅ Agregamos pestañas con otras páginas
    tabs_view = ft.Tabs(
        selected_index=0,
        tabs=[
            #ft.Tab(text="Inicio", content=main_view),  # ✅ Agregamos la vista principal
            ft.Tab(text="Inicio", content=ft.Column( controls=[main_view] )),  # ✅ Agregamos la vista principal
            ft.Tab(text="Configuración", content=ft.Text("Aquí irían las configuraciones")),
            ft.Tab(text="Acerca de", content=ft.Text("Información sobre la app"))
        ]
    )
    page.add(tabs_view)  # ✅ Agregamos las vistas a la página

ft.app(target=main)
