# Buenas prácticas para la creación de botones en Flet
Cuando trabajamos con Flet y queremos hacer botones reutilizables y flexibles, es importante seguir buenas prácticas de programación. Te compartiré algunas estrategias clave y te mostraré cómo yo lo manejaría.

## 1. Definir una clase base para los botones
En lugar de crear múltiples clases para cada tipo de botón, es mejor crear una clase base que nos permita personalizar fácilmente los botones según nuestras necesidades.

✅ Ventajas de esto:

Código más reutilizable.
Separa la lógica de presentación de la lógica del negocio.
Fácil de extender para agregar nuevos tipos de botones.1. Definir una clase base para los botones
En lugar de crear múltiples clases para cada tipo de botón, es mejor crear una clase base que nos permita personalizar fácilmente los botones según nuestras necesidades.

✅ Ventajas de esto:

Código más reutilizable.
Separa la lógica de presentación de la lógica del negocio.
Fácil de extender para agregar nuevos tipos de botones.

## 2. Ejemplo de una clase base para botones
Aquí está un diseño limpio y flexible de una clase CustomButton, que nos permite crear cualquier tipo de botón con diferentes estilos y eventos.

```py
import flet as ft

class CustomButton(ft.UserControl):
    def __init__(self, text:str, icon=None, bgcolor=ft.colors.BLACK12, text_color= ft.colors.WHITE, on_click= None, button_type = "elevated"):
        """
        Clase base para botones personalizados en Flet.

        :param text: Texto del boton.
        :param icon: Icono opcional.
        :param bgcolor: Color de fondo.
        :param text_color: Color del texto.
        :param on_click: Funcion que se ejecutara al hacer clic.
        :param button_type: Tipo de boton ('elevated', 'floating', 'outlined').
        """
        super().__init__()
        self.text = text
        self.icon = icon
        self.bgcolor = bgcolor
        self.text_color = text_color
        self.on_click = on_click
        self.button_type = button_type
        self.button = None  # Guardamos la referencia al boton, Se inicializará en `build()`


    def on_click_handler(self, e):
        """
        Metodo base para manejar clcks en el boton..
        Se puede sobrescribir en subclases
        """
        if self.on_click:
            self.on_click(e) # Ejecuta la funcion proporcionada


    def build(self):
        """
        Construye el boton basado en el tipo seleccionado.
        """
        if self.button_type == "elevated":
            self.button = ft.ElevatedButton(
                text=self.text,
                icon=self.icon,
                bgcolor=self.bgcolor,
                color=self.text_color,
                on_click=self.on_click_handler
            )
        elif self.button_type == "floating":
            self.button = ft.FloatingActionButton(
                text=self.text,
                icon=self.icon,
                bgcolor=self.bgcolor,
                on_click=self.on_click_handler
            )
        elif self.button_type == "outlined":
            self.button = ft.OutlinedButton(
                text=self.text,
                icon=self.icon,
                on_click=self.on_click_handler
            )
        else:
            raise ValueError("Tipo de boton no soportado. Usa 'elevated', 'floating' o 'outlined'.")

        return self.button
```

## 3. Cómo usar esta clase de botones
Ahora podemos crear distintos botones con diferentes estilos y acciones.

```py
def main(page: ft.Page):
    page.title = "Ejemplo de Botones"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    def button_click(e):
        print("¡Botón presionado!")

    # Botón Elevado
    btn1 = CustomButton(text="Aceptar", on_click=button_click, button_type="elevated")

    # Botón Flotante con icono
    btn2 = CustomButton(text="Añadir", icon=ft.icons.ADD, button_type="floating")

    # Botón con borde
    btn3 = CustomButton(text="Cancelar", button_type="outlined")

    page.add(btn1, btn2, btn3)

ft.app(target=main)


```


## 4. ¿Qué logramos con esta implementación?
- ✔ Botones reutilizables y flexibles
- ✔ Fácil de personalizar (diferentes colores, iconos y tipos)
- ✔ Separa la lógica de la UI y de los eventos
- ✔ Permite extender la funcionalidad sin modificar el código base

Ahora, en cualquier parte de tu código, puedes crear botones sin repetir código y sin preocuparte por cómo están implementados.

## 5. Agregar eventos dinámicamente
Si necesitas que un botón haga cosas más avanzadas, puedes permitirle recibir eventos personalizados.
```py
def show_alert(e):
    print("Alerta: Se presionó un botón")

btn_alert = CustomButton(text="Alerta", on_click=show_alert)

```
## 6. Extender la clase para más funcionalidades
Si en el futuro quieres agregar más opciones, puedes extender esta misma clase.
Por ejemplo, podríamos hacer que el botón cambie de color cuando se presiona.

```py
class StateButton(CustomButton):
    def __init__(self, text, icon=None, bgcolor=ft.colors.BLACK12,
                  text_color=ft.colors.WHITE, on_click=None, button_type="elevated"):
        """
        Boton que cambia de color cuando se presiona.
        """
        super().__init__(text, icon, bgcolor, text_color, on_click, button_type) # Llamamos al constructor de la clase padre
        self.clicked = False     # Agregamos un estado para saber si el boton ha sido presionado


    def on_click_handler(self, e):
        """
        Evento que cambia de color al boton al hacer clic.
        """
        self.clicked = not self.clicked  # Alternamos entre True y False
        print(f"Presionando boton. Estado actual: {self.clicked}")  # ✅ Confirmamos que el evento se ejecuta
        
         # ✅ Modificamos directamente el color del boton
        if self.button:
            nuevo_color = ft.colors.GREEN_500 if self.clicked else ft.colors.BLUE_500
            print(f"Cambiando color a: {nuevo_color}")  # 🔍 Debugging
            self.bgcolor = nuevo_color
                    # ✅ Actualizamos el boton dentro de `self.controls`
            self.controls.clear()  # Eliminamos el boton antiguo
            self.controls.append(self.build())  # Agregamos el boton actualizado
            self.update()  # ✅ Esto forzará que `build()` se ejecute nuevamente y actualice el boton

    def build(self):
        """
        Retorna el boton con el evento modificado
        """
        # Ahora guardamos el boton en un atributo: self.button
        print(self.bgcolor)
        self.button = ft.ElevatedButton(
            text=self.text,
            icon=self.icon,
            bgcolor=self.bgcolor,  # Usamos `self.bgcolor`
            color=self.text_color,
            on_click=self.on_click_handler  # Asociamos nuestro propio evento
        )
        return self.button  # Retornamos el boton almacenado
```

Ahora, cuando el usuario haga clic, el botón cambiará de color.


# Consejos adicionales para mejorar la gestión de botones
Usa un ``factory method`` si tienes botones muy específicos

Si en tu app siempre usas botones con el mismo estilo, puedes definir métodos que generen estos botones de manera automática.

```py
class ButtonFactory:
    @staticmethod
    def primary_button(text, on_click=None):
        return CustomButton(text=text, bgcolor=ft.colors.BLUE_500, on_click=on_click)

    @staticmethod
    def danger_button(text, on_click=None):
        return CustomButton(text=text, bgcolor=ft.colors.RED_500, on_click=on_click)

```

✅ Uso:
```py
btn_ok = ButtonFactory.primary_button("Aceptar", button_click)
btn_delete = ButtonFactory.danger_button("Eliminar", button_click)
```



## Resumen Final
- ``ft.UserControl`` es la mejor opción para crear botones reutilizables.
- Separa la lógica de eventos de la interfaz gráfica.
- Usa ``button_type`` para definir diferentes estilos de botones en la misma clase.
- Implementa ``factory methods`` si tienes muchos botones similares.
- Puedes agregar eventos dinámicos fácilmente.
- Extiende la clase base para agregar funcionalidades sin modificarla directamente.

Con esta estructura, ¡podrás crear cualquier botón que necesites de manera profesional y limpia!


# paso a paso de la clase CustomButton()

Ahora desglosaremos cada parte del código, explicando su propósito.

## 1️⃣ Creación de la clase base CustomButton
```py
class CustomButton(ft.UserControl):
```
#### 📌 Esta clase define un botón reutilizable en Flet.

✅ Hereda de ``ft.UserControl``, lo que significa que puede contener otros widgets y actualizarse cuando sea necesario.

#### 2️⃣ Constructor __init__()
```py
def __init__(self, text: str, icon=None, bgcolor=ft.colors.BLACK12, 
             text_color=ft.colors.WHITE, on_click=None, button_type="elevated"):
```
Este método define los atributos del botón.

## 🔹 Explicación de los parámetros:


- Parámetro	Explicación
- text	Texto del botón.
- icon	Ícono opcional del botón.
- bgcolor	Color de fondo del botón.
- text_color	Color del texto del botón.
- on_click	Función que se ejecutará cuando se haga clic en el botón.
- button_type	Tipo de botón: "elevated", "floating", "outlined".

## 🔹 Almacena los valores en self para usarlos 
```py
self.text = text
self.icon = icon
self.bgcolor = bgcolor
self.text_color = text_color
self.on_click = on_click
self.button_type = button_type

```
Esto permite que estos valores estén disponibles dentro de la clase y se puedan modificar más tarde.

## 3️⃣ Método build()
#### Lógica de build()
```py
if self.button_type == "elevated":
    return ft.ElevatedButton(
        text=self.text,
        icon=self.icon,
        bgcolor=self.bgcolor,
        color=self.text_color,
        on_click=self.on_click_handler
    )
```

- ✅ Este código genera el botón en función del tipo (elevated, floating, etc.).
- ✅ Se asocia el evento on_click_handler al botón para que pueda detectar los clics


# 📌 Paso a paso de StateButton
Ahora vamos a la clase StateButton, que hereda de CustomButton, pero agrega la funcionalidad de cambiar de color al hacer clic.

## 1️⃣ Constructor __init__()
```
class StateButton(CustomButton):
    def __init__(self, text, icon=None, bgcolor=ft.colors.BLACK12, 
                 text_color=ft.colors.WHITE, on_click=None, button_type="elevated"):

```
📌 Este constructor inicializa un botón especial que cambia de color al hacer clic.

✅ Llama a super().__init__() para usar la lógica de CustomButton

```py
super().__init__(text, icon, bgcolor, text_color, on_click, button_type)
```

✅ Se agrega una nueva variable de estado llamada self.clicked

```py
self.clicked = False  # Estado inicial del botón

```
Esta variable almacena si el botón ha sido presionado o no.

## 2️⃣ Método on_click_handler()
```py
def on_click_handler(self, e):
```
📌 Este método maneja el evento cuando el botón es presionado.

✅ Alterna entre True y False cada vez que se presiona el botón

```py
self.clicked = not self.clicked  # Alternamos entre True y False

```
✅ Cambia el color del botón en función del estado
```py
self.bgcolor = ft.colors.GREEN_500 if self.clicked else ft.colors.BLUE_500
```

✅ Actualiza el botón para reflejar el cambio de color
```py
self.controls.clear()  # 🔹 Borra el botón antiguo
self.controls.append(self.build())  # 🔹 Agrega el botón con el nuevo color
self.update()  # 🔹 Le dice a Flet que debe redibujar el UserControl
```

## 3️⃣ Método build()
```py
def build(self):
```
📌 Este método crea el botón y se ejecutará nuevamente cada vez que el color cambie.

✅ Cada vez que on_click_handler() cambia el color, build() se ejecuta con el nuevo color
```
print(f"Ejecutando build() con color {self.bgcolor}")  # 🔍 Debugging
```

✅ Se crea el botón con el color actualizado

```py
self.button = ft.ElevatedButton(
    text=self.text,
    icon=self.icon,
    bgcolor=self.bgcolor,
    color=self.text_color,
    on_click=self.on_click_handler  
)
return self.button  
```
- 🔹 Flet usa este nuevo botón para reemplazar el anterior en la interfaz.

# 📌 ¿Cómo se actualiza el color?

📌 Cuando hacemos clic en el botón, ``on_click_handler()`` hace lo siguiente:

- 1️⃣ Cambia el estado del botón ``(self.clicked)``
- 2️⃣ Cambia el color de fondo ``(self.bgcolor)``
- 3️⃣ Elimina el botón antiguo ``(self.controls.clear())``
- 4️⃣ Crea un nuevo botón con el color actualizado ``(self.controls.append(self.build()))``
- 5️⃣ Ejecuta ``self.update()`` para que Flet redibuje el botón

💡 Así garantizamos que Flet detecte el cambio y lo refleje en la UI.

# 📌 Resumen final

|Concepto | Explicacion |
|----|----|
|``build()``|Se ejecuta cuando el botón se construye o cambia de estado.|
|``self.bgcolor``|Almacena el color actual del botón.|
|``self.clicked``|Indica si el botón ha sido presionado o no.|
|``self.controls.clear()``|Borra el botón anterior antes de agregar uno nuevo.|
|``self.controls.append(self.build())``|Crea un nuevo componente|
|``self.update()``|Fuerza la reconstrucción del ``UserControl`` para reflejar los cambios.|


# 📌 Conclusión
- ✅ Ahora entiendes cómo Flet maneja la actualización de componentes.
- ✅ Puedes replicar este patrón para cualquier otro UserControl.
- ✅ Si quieres agregar más efectos (como cambiar el tamaño o el texto), puedes modificar on_click_handler().

🚀 ¡Ahora puedes usar este conocimiento para construir interfaces dinámicas en Flet! 🎉