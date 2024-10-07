# Flet

Flet is a framework that allows building interactive multi-user web,  desktop and mobile applications in your favorite language without prior experience in front-end development.

you build a UI for you program with flet control wich are based on flutter by Google. Flet does not  just ``wrap`` flutter widgets,  but adds its own ``opinion`` by combining a smaller widgets, hiding complexities, implementing UI best practices, applying reasonable defaults, all to ensure your app look cool and profesional without extra efforts.

[Doc Oficial](https://flet.dev/docs/guides/python/getting-started)

# Flex app example

Here is a sample ``counter`` app

```py
import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
# run the app as a  web browser app,
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
```

Now if you want to run the app as a  web browser app, just replace the last line with: 
```py
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
```

# Ports INFO
Internally, every Flet app is a web app and even if it's opened in a native OS window a built-in web server is still started on a background. Flet web server is called "Fletd" and by default it's listening on a random TCP port. You can specify a custom TCP port and then open the app in the browser along with desktop view:

```py
flet.app(port=8550, target=main)
```
Open http://localhost:<port> in your browser to see web version of your Flet app.


# cotroles basicos

# Clase 1: Introducción a los Controles Básicos

Los controles básicos son los elementos fundamentales que conforman una interfaz de usuario en Flet. Vamos a revisar algunos de los más comunes:

   - Controles que Veremos Hoy:
   - Text: Muestra texto en la pantalla.
   - Button: Un botón interactivo que realiza una acción cuando es presionado.
   - TextField: Un campo de entrada de texto.
   - Row y Column: Para organizar otros controles horizontal o verticalmente.

   ## Ejemplo 1: Uso de Text y Button

```py
import flet as ft

def main(page: ft.Page):
    # Crear un texto
    hello_text = ft.Text("Hola, mundo!", size=20)

    # Crear un boton que cambiara el texto al ser presionado
    def button_click(e):
        hello_text.value = "¡Boton presionado!"
        page.update()

    # Crear un boton
    button = ft.ElevatedButton("Presionar", on_click=button_click)

    # Añadir los controles a la pagina
    page.add(hello_text, button)

ft.app(target=main)
```

### Explicación:
- ``ft.Text("Hola, mundo!", size=20)``: Muestra un texto en la pantalla con un tamaño de fuente de 20.
- ``ft.ElevatedButton("Presionar", on_click=button_click)``: Crea un botón elevado que llama a la función button_click cuando es presionado.
- ``page.update()``: Actualiza la pantalla para reflejar los cambios después de cambiar el valor del texto.

# Ejemplo 2: Uso de TextField (Campo de Texto)

```py
import flet as ft

def main(page: ft.Page):
    # Crear un campo de texto
    text_input = ft.TextField(label="Escribe algo", width=200)

    # Crear un texto que mostrará lo que el usuario escribió
    result_text = ft.Text()

    # Crear un botón que tomará el texto del campo de texto y lo mostrará
    def submit_click(e):
        result_text.value = f"Has escrito: {text_input.value}"
        page.update()

    # Botón para enviar
    submit_button = ft.ElevatedButton("Enviar", on_click=submit_click)

    # Añadir los controles a la página
    page.add(text_input, submit_button, result_text)

ft.app(target=main)
```

## Explicación:
- ``ft.TextField(label="Escribe algo", width=200)``: Crea un campo de texto con una etiqueta.
- ``ft.Text()``: Se usa para mostrar el texto que el usuario introdujo en el campo de texto.
- ``submit_click``: Toma el valor del campo de texto cuando se presiona el botón y actualiza el texto con lo que el usuario escribió.

# Ejemplo 3: Organización con Row y Column

Puedes organizar los controles en filas y columnas para crear una estructura más ordenada.

```py
import flet as ft

def main(page: ft.Page):
    # Crear un campo de texto
    text_input = ft.TextField(label="Escribe algo", width=200)
    result_text = ft.Text()

    # Crear un botón que toma el texto y lo muestra
    def submit_click(e):
        result_text.value = f"Has escrito: {text_input.value}"
        page.update()

    submit_button = ft.ElevatedButton("Enviar", on_click=submit_click)

    # Organizar en una fila
    row = ft.Row([text_input, submit_button])

    # Organizar en una columna
    page.add(row, result_text)

ft.app(target=main)
```

## Explicación:
``ft.Row([text_input, submit_button])``: Coloca el campo de texto y el botón uno al lado del otro en una fila.
``page.add(row, result_text)`` : Añade la fila y el texto a la página.

# Actividad: Crear un Formulario Básico
Objetivo: Crea un formulario básico que tenga los siguientes elementos:

- Un campo de texto para ingresar el nombre.
- Un campo de texto para ingresar el correo electrónico.
- Un botón que, al presionarse, muestre un mensaje con los valores de ambos campos.
- ``Pista``: Usa los controles TextField, ElevatedButton, Text, y organiza todo en un Column para que los elementos aparezcan uno debajo del otro.

# Clase 2: Creando Componentes Reutilizables
¿Por qué crear componentes reutilizables?

Crear componentes reutilizables te permite escribir código que puedes usar en diferentes partes de la aplicación sin duplicarlo. Por ejemplo, podrías crear una clase FormField que encapsule un campo de texto con su respectiva etiqueta.

## Ejemplo: Componente Reutilizable FormField
```py
class FormField(ft.UserControl):
    def __init__(self, label, width=200):
        super().__init__()
        self.label = label
        self.width = width
        self.text_field = ft.TextField(label=self.label, width=self.width)

    def get_value(self):
        return self.text_field.value

    def build(self):
        return self.text_field
```
### Usando el Componente Reutilizable:

```py
import flet as ft
from form_field import FormField  # Asume que guardaste el componente en un archivo llamado form_field.py

def main(page: ft.Page):
    # Crear dos campos reutilizables
    name_field = FormField("Nombre")
    email_field = FormField("Correo Electrónico")

    # Crear un texto que mostrará los valores
    result_text = ft.Text()

    # Función para el botón
    def submit_click(e):
        result_text.value = f"Nombre: {name_field.get_value()}, Correo: {email_field.get_value()}"
        page.update()

    submit_button = ft.ElevatedButton("Enviar", on_click=submit_click)

    # Añadir los campos y el botón
    page.add(name_field, email_field, submit_button, result_text)

ft.app(target=main)
```
## Explicación:
- ``Clase FormField``: Es un componente reutilizable que encapsula un campo de texto. Tiene un método get_value para obtener el valor del campo.
- ``name_field`` y ``email_field``: Son instancias de la clase FormField, que representan campos de entrada reutilizables.


# Actividad: Crear Componentes Reutilizables
- ``Tarea``: Crea una clase ButtonGroup que encapsule dos botones, uno de "Aceptar" y otro de "Cancelar".
- ``Desafío``: Usa tu clase ButtonGroup en una aplicación y muestra qué botón fue presionado.

Con este enfoque modular y paso a paso, aprenderás a dominar los controles básicos en Flet, junto con la creación de componentes reutilizables que harán que tu código sea más limpio, fácil de mantener y escalable.