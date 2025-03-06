# 📌 1️⃣ ¿Dónde manejar las Tabs?

Tienes dos opciones principales:

| Enfoque |	Ventajas |	Desventajas |
|---- | ---- | ---- |
| Manejar Tabs en main.py| 	Simplicidad., Se definen todas las pestañas en un solo lugar.| Si la app crece, el código de main.py se vuelve difícil de mantener.| 
| Crear una clase MainView para manejar Tabs (✅ RECOMENDADO)| 	Código más organizado., Se pueden agregar más vistas sin modificar main.py. |- Hay que estructurar la app desde el principio.| 


- 🔹 Para apps pequeñas, puedes manejar Tabs en main.py.
- 🔹 Para apps medianas y grandes, es mejor crear una clase MainView para centralizar la navegación.

✅ Si planeas escalar la app (agregar más páginas, soporte móvil, etc.), lo mejor es manejar Tabs en MainView.

## 📌 2️⃣ Cómo estructurar la app correctamente
Si queremos mantener la app bien organizada, podemos usar una estructura como esta:

```bash
/iot_app
│── /src
│   ├── /views
│   │   ├── mainview.py  # 📌 Vista principal (maneja las pestañas y la navegación)
│   │   ├── homeview.py  # 📌 Página principal (Home)
│   │   ├── settingsview.py  # 📌 Página de Configuración
│   │   ├── aboutview.py  # 📌 Página Acerca de
│   ├── /components
│   │   ├── customcontainer.py
│   │   ├── customcolumn.py
│   │   ├── custombutton.py
│   ├── main.py  # 📌 Archivo principal
```
### 📌 Cada página (View) se maneja en un archivo separado.
### 📌 MainView contiene las pestañas y la navegación general.

#### ✅ Ventajas de esta estructura:

- ✔ Código modular y organizado.
- ✔ Facilita la escalabilidad y la integración de más vistas.
- ✔ Podemos agregar más vistas fácilmente sin modificar main.py.


### 📌 3️⃣ Implementación en MainView
### 📍 Archivo: views/mainview.py

```py
import flet as ft
from views.homeview import HomeView
from views.settingsview import SettingsView
from views.aboutview import AboutView

class MainView(ft.UserControl):
    """
    Clase principal que maneja la navegación y las pestañas de la aplicación.
    """

    def __init__(self):
        super().__init__()

    def build(self):
        """
        Construye la interfaz principal con las pestañas (Tabs).
        """
        self.tabs = ft.Tabs(
            selected_index=0,
            animation_duration=300,  # ✅ Animación suave al cambiar pestañas
            tabs=[
                ft.Tab(text="Inicio", content=HomeView()),  # 📌 Página de inicio
                ft.Tab(text="Configuración", content=SettingsView()),  # 📌 Página de configuración
                ft.Tab(text="Acerca de", content=AboutView())  # 📌 Página de información
            ]
        )

        return self.tabs  # ✅ Retornamos las pestañas
```

- ✅ Esta clase se encarga de manejar la navegación de toda la app.
- ✅ Cada Tab carga una vista diferente (HomeView, SettingsView, AboutView).
- ✅ Usamos animation_duration=300 para una transición más fluida entre pestañas.

### 📌 4️⃣ Creando las diferentes vistas
### 📍 Archivo: views/homeview.py

```py
import flet as ft

class HomeView(ft.UserControl):
    """
    Página de Inicio.
    """

    def build(self):
        return ft.Container(
            content=ft.Text("Bienvenido a la aplicación", size=24, weight="bold"),
            padding=20,
            alignment=ft.alignment.center
        )

```
### 📍 Archivo: views/settingsview.py

```py
import flet as ft

class SettingsView(ft.UserControl):
    """
    Página de Configuración.
    """

    def build(self):
        return ft.Container(
            content=ft.Text("Configuración", size=24, weight="bold"),
            padding=20,
            alignment=ft.alignment.center
        )
```

### 📍 Archivo: views/aboutview.py

```py
import flet as ft

class AboutView(ft.UserControl):
    """
    Página Acerca de.
    """

    def build(self):
        return ft.Container(
            content=ft.Text("Acerca de esta aplicación", size=24, weight="bold"),
            padding=20,
            alignment=ft.alignment.center
        )
```
- ✅ Cada vista (View) está separada en su propio archivo para mantener el código modular.
- ✅ Cada vista es un UserControl con su propio contenido.

### 📌 5️⃣ Modificar main.py para cargar MainView
### 📍 Archivo: main.py

```py
import flet as ft
from views.mainview import MainView

def main(page: ft.Page):
    page.title = "Aplicación con Pestañas"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # ✅ Centramos todo

    # ✅ Creamos una instancia de `MainView`
    main_view = MainView()

    page.add(main_view)  # ✅ Agregamos `MainView` a la página

ft.app(target=main)
```

- ✅ Aquí simplemente importamos MainView y lo mostramos en main.py.
- ✅ La navegación se maneja dentro de MainView, manteniendo main.py limpio.

### 📌 🚀 Beneficios de esta estructura
 |Beneficio |	Explicación |
| ---- | ---- |
 |✅ Código modular |	Cada vista (View) está en un archivo separado. |
 |✅ Escalabilidad |	Podemos agregar más vistas sin modificar main.py. |
 |✅ Manejo limpio de Tabs |	MainView se encarga de la navegación sin sobrecargar main.py. |
 |✅ Soporte futuro para móvil |	Esta estructura facilita una futura migración a Flet Mobile. |

# 📌 🚀 Resumen Final
- 1️⃣ Separamos la navegación en MainView.
- 2️⃣ Cada pestaña (Tab) carga una vista (HomeView, SettingsView, AboutView).
- 3️⃣ main.py solo carga MainView, manteniéndolo limpio y organizado.
- 4️⃣ La app ahora es modular, escalable y lista para más integraciones.

💡 ¡Ahora tienes una estructura profesional y organizada para manejar pestañas y navegación en Flet!