import flet as ft
from tabs.administrar_esp32_tab import AdministrarESP32Tab
from tabs.visualizar_datos_tab import VisualizarDatosTab
from tabs.configuracion_tab import ConfiguracionTab
from utils.mqtt_manager import mqtt_manager

def main(page: ft.Page):
    page.title = "ESP32 IoT Dashboard"
    page.scroll = "auto"

    # Crear instancias de las pestañas solo una vez
    admin_tab = AdministrarESP32Tab(mqtt_manager)
    visualizar_tab = VisualizarDatosTab(mqtt_manager)
    configuracion_tab = ConfiguracionTab()

    content_container = ft.Container(content=admin_tab)

    def tab_changed(e=None):
        selected_tab = tabs.tabs[tabs.selected_index].text
        if selected_tab == "Administrar ESP32":
            content_container.content = admin_tab  # No se recrea la pestaña
        elif selected_tab == "Visualizar Datos":
            content_container.content = visualizar_tab
        elif selected_tab == "Configuración":
            content_container.content = configuracion_tab
        page.update()

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="Administrar ESP32"),
            ft.Tab(text="Visualizar Datos"),
            ft.Tab(text="Configuración"),
        ],
        on_change=tab_changed
    )

    page.add(tabs, content_container)
    tab_changed()

if __name__ == "__main__":
    ft.app(target=main)