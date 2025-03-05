# 📌 ¿Cómo funciona Flet internamente?
🔹 Arquitectura de Flet
Flet se basa en un modelo de UI declarativa y reactiva, similar a Flutter, donde la interfaz de usuario (UI) se define en clases y se actualiza dinámicamente en función de los cambios de estado.

- 1️⃣ Se construyen componentes (UserControl, Column, Row, ElevatedButton, etc.).
- 2️⃣ Se ejecuta el método build() de los controles para renderizarlos.
- 3️⃣ Cuando un evento cambia un valor, se llama update() para reflejar los
cambios.
- 4️⃣ Flet detecta las modificaciones y re-renderiza los widgets necesarios en la UI.

## 📌 Clases y métodos clave en Flet
### 🔹 UserControl: La base de los componentes personalizados
``UserControl`` es una clase especial en Flet que permite crear componentes reutilizables con su propio estado y lógica.

📌 Ejemplo de un UserControl básico:
```py
import flet as ft

class MyComponent(ft.UserControl):
    def build(self):
        return ft.Text("¡Hola desde un UserControl!")

def main(page: ft.Page):
    page.add(MyComponent())

ft.app(target=main)

```

✅ ``MyComponent`` es un widget personalizado que se puede reutilizar.

### 📌 Métodos esenciales en Flet
Ahora veremos los métodos más importantes de ``UserControl`` y cuándo usarlos.
#### 🔹 1. ``build()``: Construcción del widget
- 📌 ``build()`` define cómo se verá el componente en la UI. Se ejecuta cuando se crea el control y cada vez que llamamos update().

✅ Ejemplo:
```py
class MyComponent(ft.UserControl):
    def build(self):
        print("Ejecutando build()")
        return ft.Text("¡Hola desde Flet!")
```
💡 ``build()`` debe devolver un widget o lista de widgets.


#### 🔹 2. update(): Refrescar el control
- 📌 update() se usa para actualizar la UI después de un cambio de estado. Cuando llamamos a update(), Flet vuelve a ejecutar build() y redibuja el control.

✅ Ejemplo:
```
class Counter(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.count = 0

    def increment(self, e):
        self.count += 1
        self.update()  # Forzar la actualización de la UI

    def build(self):
        return ft.Column([
            ft.Text(f"Contador: {self.count}", key="counter_text"),
            ft.ElevatedButton("Incrementar", on_click=self.increment)
        ])

```

💡 Cada vez que ``increment()`` cambia ``self.count``, ```update()``` reconstruye ``build() ``para reflejar el cambio.


#### 🔹 3. before_update(): Antes de actualizar
📌 ``before_update()`` se ejecuta antes de ``update()``, útil si necesitas validar o modificar datos antes de redibujar la UI.

✅ Ejemplo:
```py
class Example(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.count = 0

    def before_update(self):
        print(f"Antes de actualizar: count = {self.count}")

    def increment(self, e):
        self.count += 1
        self.update()

    def build(self):
        return ft.Text(f"Contador: {self.count}")

```
💡 Se ejecuta antes de que build() se llame nuevamente.

#### 🔹 4. did_mount(): Cuando el componente se carga
📌`` did_mount()`` se ejecuta cuando el componente se agrega a la UI por primera vez.

✅ Es útil para inicializar datos o suscribirse a eventos.

✅ Ejemplo:
```py
class Example(ft.UserControl):
    def did_mount(self):
        print("¡El componente se ha montado en la UI!")

    def build(self):
        return ft.Text("¡Hola desde Flet!")
```

#### 🔹 5. will_unmount(): Antes de que el componente se elimine
📌 will_unmount() se ejecuta cuando el componente va a ser eliminado de la UI.

✅ Ejemplo:
```py
class Example(ft.UserControl):
    def will_unmount(self):
        print("El componente se eliminará")

    def build(self):
        return ft.Text("¡Este componente será removido!")

```
💡 Útil para limpiar eventos, desconectar sockets o guardar datos antes de salir.

## 📌 Resumen de métodos esenciales en Flet

|Método|	¿Cuándo se ejecuta?	| ¿Para qué sirve?|
| ---- | ---- | ---- |
|build()|	Cuando se construye o se actualiza un control|	Define la estructura del widget
|update() |	Cuando queremos reflejar cambios en la UI|	Vuelve a llamar build()
|before_update() |	Justo antes de update()|	Validaciones previas
|did_mount() |	Cuando el control se monta en la UI|	Inicializar datos, suscripciones
|will_unmount() |	Antes de que el control se elimine|	Liberar recursos, limpiar eventos|



# 📌 Estructura recomendada para proyectos en Flet
Si estás construyendo una aplicación más grande, la mejor práctica es estructurar el código en múltiples archivos.

📌 Ejemplo de estructura de carpetas para una app en Flet
```bash
/mi_proyecto
│── main.py             # Punto de entrada de la aplicación
│── /components         # Componentes reutilizables
│   │── button_factory.py
│   │── state_button.py
│── /pages              # Páginas de la aplicación
│   │── home.py
│   │── settings.py
│── /utils              # Funciones auxiliares
│   │── helpers.py

```
### 📌 Ejemplo final: Aplicación estructurada
```
import flet as ft
from components.button_factory import ButtonFactory
from pages.home import HomePage

def main(page: ft.Page):
    page.title = "Mi App en Flet"
    page.add(HomePage())

ft.app(target=main)

```
✅ Esto permite una mejor organización y escalabilidad.


## 📌 Conclusión Final
Ahora entiendes cómo funciona Flet internamente y los métodos esenciales para trabajar con UserControl:

- 1️⃣ build() → Construye el UI del componente.
- 2️⃣ update() → Redibuja el UI cuando cambia el estado.
- 3️⃣ before_update() → Permite validar antes de actualizar.
- 4️⃣ did_mount() → Se ejecuta al cargar el componente en la UI.
- 5️⃣ will_unmount() → Se ejecuta antes de eliminar el componente.

📌 Con este conocimiento, puedes construir aplicaciones escalables y organizadas en Flet utilizando clases y estructuras adecuadas. 🚀🔥





# Flet componentes personalizados
 Usamos ``ft.UserControl``, que nos permite crear componentes personalizados que contienen varios elementos.

## ¿Que es ft.UserControl y por que lo usamos?
``ft.UserControl`` es una clase base en Flet que permite crear componentes reutilizables.
Al heredar de ft.UserControl, podemos definir una estructura mas flexible, permitiendonos agregar cualquier cantidad de controles

## Por ejemplo:
    El problematica al usar un componente especifico como ``ft.ElevatedButton``, este componente solo heredara las propiedades de 
    ft.ElevatedButton, el cual solo sera un botón individual y no permite agregar más controles dentro de él, mas que los que la clase de flet permite.

    ✅ Solución: Usamos ft.UserControl, que nos permite crear componentes personalizados que contienen varios elementos.


- ✔ Herencia de ft.UserControl para componer varios widgets.
- ✔ Uso del método build() para retornar la estructura de la UI.




# Factory method

## 📌 ¿Qué es un Factory Method?
📌 Un Factory Method (Método de Fábrica) es un patrón de diseño que nos ayuda a crear objetos sin necesidad de instanciarlos directamente dentro de nuestro código principal.

En este caso, podemos usarlo para crear diferentes tipos de botones de manera dinámica sin repetir código innecesario.

🎯 ¿Por qué usar Factory Methods en Flet?
Si tienes muchos botones similares (por ejemplo, con diferentes colores, tamaños o eventos), en lugar de escribir cada botón manualmente, puedes crear un método que genere botones automáticamente con ciertos parámetros.


✅ Ventajas de usar Factory Methods en Flet
- ✔ Reutilización de código: No necesitas escribir cada botón manualmente.
- ✔ Mayor flexibilidad: Puedes cambiar fácilmente los parámetros de los botones sin modificar el código principal.
- ✔ Facilita la escalabilidad: Si en el futuro necesitas agregar más botones con ligeros cambios, solo modificas la fábrica.


## 📌 Ejemplo práctico
Supongamos que queremos generar múltiples botones con diferentes colores y eventos de manera más eficiente.

Sin Factory Methods, podríamos hacer algo así:
```py
btn1 = CustomButton(text="Aceptar", bgcolor=ft.colors.GREEN, on_click=lambda e: print("Aceptado"))
btn2 = CustomButton(text="Cancelar", bgcolor=ft.colors.RED, on_click=lambda e: print("Cancelado"))
btn3 = CustomButton(text="Reintentar", bgcolor=ft.colors.ORANGE, on_click=lambda e: print("Reintentando..."))

```

📌 El problema aquí es que cada botón se crea manualmente, lo que no es eficiente si necesitas muchos botones.

# ✅ Solución con Factory Methods
Podemos crear una función que fabrique botones automáticamente en función de ciertos parámetros.

🔹 Factory Method para generar botones
```py
def create_button(text, color, action):
    return CustomButton(text=text, bgcolor=color, on_click=action)
```
✅ Ahora podemos usar esta función para crear botones de manera más eficiente:
```py
btn1 = create_button("Aceptar", ft.colors.GREEN, lambda e: print("Aceptado"))
btn2 = create_button("Cancelar", ft.colors.RED, lambda e: print("Cancelado"))
btn3 = create_button("Reintentar", ft.colors.ORANGE, lambda e: print("Reintentando..."))

```
📌 Esto es mucho más limpio y fácil de mantener.

## 📌 Otro Ejemplo: Factory Method para StateButton

Si queremos generar múltiples StateButton que cambien de color, podemos crear una función que los fabrique.

```py
def create_state_button(text):
    return StateButton(text=text)
```
✅ Ahora podemos crear varios botones dinámicamente:
```py
btn1 = create_state_button("Botón 1")
btn2 = create_state_button("Botón 2")
btn3 = create_state_button("Botón 3")
```
📌 Esto nos permite generar StateButton fácilmente sin repetir código.

# 📌 ¿Cuándo usar Factory Methods en Flet?
- ✅ Cuando tienes múltiples botones con pequeñas variaciones (color, texto, eventos, etc.).
- ✅ Cuando necesitas generar dinámicamente botones sin repetir código.
- ✅ Cuando quieres hacer tu código más escalable y fácil de modificar en el futuro.

## 🚀 Resumen Final

|Enfoque|	¿Cómo funciona?	Ventajas|
| ---- | ---- |
|Código manual|	Escribes cada botón individualmente	Funciona, pero es repetitivo|
Factory Method|	Usas una función que crea botones dinámicamente	Código más limpio y reutilizable|

💡 Usar Factory Methods te ayuda a organizar mejor tu código y te permite agregar eventos dinámicos con facilidad. 🚀🔥

🔹 Ahora puedes generar botones dinámicos sin esfuerzo en Flet y escalarlos sin problemas. 🎉


# 📌 Opciones para implementar Factory Methods en Flet

🔹 Opción 1: Usar una función independiente (más simple)
Si solo necesitas generar botones y no necesitas almacenamiento adicional, puedes usar una función fuera de cualquier clase.

🔹 Opción 2: Usar un Factory Method dentro de una clase
Si trabajas con múltiples tipos de botones y necesitas flexibilidad y reutilización, una clase que maneje la creación de botones es la mejor opción.

## ✅ Opción 1: Factory Method como función independiente

📌 Si solo necesitas crear botones simples de forma dinámica, esta es la mejor opción.
Aquí creamos una función create_button que fabrica botones personalizados.

```py
import flet as ft

def create_button(text, color, action):
    """
    Factory Method para crear un botón personalizado.
    :param text: Texto del botón.
    :param color: Color de fondo del botón.
    :param action: Función a ejecutar cuando se presiona el botón.
    :return: Un botón de tipo ElevatedButton en Flet.
    """
    return ft.ElevatedButton(
        text=text,
        bgcolor=color,
        on_click=action
    )

def main(page: ft.Page):
    page.title = "Ejemplo de Factory Method en Flet"
    
    # ✅ Creamos botones dinámicamente con la función `create_button`
    btn1 = create_button("Aceptar", ft.colors.GREEN, lambda e: print("Aceptado"))
    btn2 = create_button("Cancelar", ft.colors.RED, lambda e: print("Cancelado"))
    btn3 = create_button("Reintentar", ft.colors.ORANGE, lambda e: print("Reintentando..."))

    page.add(btn1, btn2, btn3)

ft.app(target=main)

```

### 🚀 Ventajas de esta opción
- ✅ Código más limpio y reutilizable.
- ✅ No es necesario definir una clase extra.
- ✅ Ideal si solo necesitas crear botones sin almacenar información adicional.

## ✅ Opción 2: Usar una Clase con un Factory Method
📌 Si quieres mayor control sobre la creación de botones y necesitas almacenar configuraciones globales, usa una clase.

Aquí creamos una clase ButtonFactory que maneja la creación de botones.

```py
import flet as ft

class ButtonFactory:
    """
    Clase que genera botones personalizados en Flet.
    """

    @staticmethod
    def create_button(text, color, action):
        """
        Factory Method estático para crear botones personalizados.
        :param text: Texto del botón.
        :param color: Color de fondo del botón.
        :param action: Función a ejecutar cuando se presiona el botón.
        :return: Un botón ElevatedButton en Flet.
        """
        return ft.ElevatedButton(
            text=text,
            bgcolor=color,
            on_click=action
        )

def main(page: ft.Page):
    page.title = "Ejemplo de Factory Method con una Clase"

    # ✅ Creamos botones dinámicamente usando la clase `ButtonFactory`
    btn1 = ButtonFactory.create_button("Aceptar", ft.colors.GREEN, lambda e: print("Aceptado"))
    btn2 = ButtonFactory.create_button("Cancelar", ft.colors.RED, lambda e: print("Cancelado"))
    btn3 = ButtonFactory.create_button("Reintentar", ft.colors.ORANGE, lambda e: print("Reintentando..."))

    page.add(btn1, btn2, btn3)

ft.app(target=main)

```

### 📌 Diferencias entre ambas opciones
| Método | Ventajas | Cuándo usarlo |
| ---- | ---- | ---- |
| Función independiente (create_button) | Simplicidad, fácil de usar | Si solo necesitas crear botones sin almacenamiento extra |
| Clase ButtonFactory con @staticmethod |	Organizado, escalable |	Si necesitas gestionar varios botones o configuraciones |

## 📌 ¿Cuál es la mejor práctica en Flet?
Si solo creas botones sin lógica extra → Usa la función (create_button).
```py
btn1 = create_button("Aceptar", ft.colors.GREEN, lambda e: print("Aceptado"))
```

### Si necesitas administrar más configuraciones → Usa una clase (ButtonFactory).
```py
btn1 = ButtonFactory.create_button("Aceptar", ft.colors.GREEN, lambda e: print("Aceptado"))
```

## 📌 🚀 Ejemplo Avanzado: Factory Method para StateButton
Si tienes botones que cambian de color, puedes crear una fábrica para StateButton:
```py
class StateButtonFactory:
    """
    Clase que genera botones de estado en Flet.
    """

    @staticmethod
    def create_state_button(text):
        return StateButton(text=text)

def main(page: ft.Page):
    page.title = "Ejemplo de Factory Method con StateButton"

    # ✅ Creamos botones que cambian de color dinámicamente
    btn1 = StateButtonFactory.create_state_button("Botón 1")
    btn2 = StateButtonFactory.create_state_button("Botón 2")
    btn3 = StateButtonFactory.create_state_button("Botón 3")

    page.add(btn1, btn2, btn3)

ft.app(target=main)

```
📌 Este método permite crear StateButton dinámicamente sin repetir código.

# 📌 Conclusión Final
- 1️⃣ Si solo necesitas crear botones de manera simple → Usa una función (create_button).
- 2️⃣ Si necesitas una estructura más organizada y escalable → Usa una clase con @staticmethod.
- 3️⃣ Si manejas StateButton u otros controles personalizados → Usa una fábrica específica (StateButtonFactory).

🚀 Ahora puedes crear botones dinámicos en Flet sin repetir código y de manera escalable. 🎉🔥


# 📌 ¿Qué es un método estático (@staticmethod)?
Un método estático es un método dentro de una clase que no necesita acceso a los atributos de la instancia (self) ni de la clase (cls).

📌 Un método estático se usa cuando la función es independiente del estado del objeto, pero sigue siendo relevante para la clase.

🎯 ¿Por qué usar @staticmethod en Flet para Factory Methods?
- 1️⃣ Evita la necesidad de instanciar la clase (ButtonFactory).
- 2️⃣ Permite reutilizar la lógica sin modificar la estructura del objeto.
- 3️⃣ Hace que el código sea más modular y limpio.


### ✅ Implementación de Factory Method con @staticmethod en Flet
📌 Ejemplo de una clase ButtonFactory que crea botones sin necesidad de instanciar la clase:

```py
import flet as ft

class ButtonFactory:
    """
    Clase que genera botones personalizados en Flet.
    """

    @staticmethod
    def create_button(text, color, action):
        """
        Factory Method estático para crear botones personalizados.

        :param text: Texto del botón.
        :param color: Color de fondo del botón.
        :param action: Función que se ejecuta al hacer clic en el botón.
        :return: Un botón ElevatedButton en Flet.
        """
        return ft.ElevatedButton(
            text=text,
            bgcolor=color,
            on_click=action
        )

def main(page: ft.Page):
    page.title = "Ejemplo de Factory Method con una Clase y @staticmethod"

    # ✅ Creamos botones dinámicamente usando el Factory Method estático
    btn1 = ButtonFactory.create_button("Aceptar", ft.colors.GREEN, lambda e: print("Aceptado"))
    btn2 = ButtonFactory.create_button("Cancelar", ft.colors.RED, lambda e: print("Cancelado"))
    btn3 = ButtonFactory.create_button("Reintentar", ft.colors.ORANGE, lambda e: print("Reintentando..."))

    page.add(btn1, btn2, btn3)

ft.app(target=main)

```

## 📌 Explicación detallada del código
🔹 1. ¿Por qué usamos @staticmethod en create_button?
```py
@staticmethod
def create_button(text, color, action):

```
- ``@staticmethod`` permite llamar a create_button sin necesidad de instanciar ButtonFactory.
- 📌 No usamos self ni cls porque create_button no necesita acceder a atributos de la instancia ni de la clase.

### 🔹 2. Llamando a create_button sin crear una instancia
```py
btn1 = ButtonFactory.create_button("Aceptar", ft.colors.GREEN, lambda e: print("Aceptado"))
```
#### ✅ Ventaja:

- No necesitas hacer factory = ButtonFactory() para usarlo.
- Solo llamas ButtonFactory.create_button(...) directamente.

🚀 Esto es útil cuando solo necesitas una función de utilidad dentro de una clase, sin crear objetos.

### 3. ¿Cómo sería sin @staticmethod?
Si no usamos ``@staticmethod``, tendríamos que crear una instancia de ButtonFactory antes de poder llamar a create_button:

```py
factory = ButtonFactory()
btn1 = factory.create_button("Aceptar", ft.colors.GREEN, lambda e: print("Aceptado"))
```
📌 Esto es innecesario porque create_button no usa atributos de la instancia.
Con @staticmethod, eliminamos este paso y llamamos el método directamente.

## 📌 ¿Cuándo usar ``@staticmethod`` en una Factory Class?

| Situación |	¿Usar @staticmethod?|
| ---- | ---- |
| Quieres crear objetos dinámicamente sin instanciar la clase |	✅ Sí |
| No necesitas modificar atributos de self o cls |	✅ Sí |
| El método solo devuelve un objeto basado en los parámetros |	✅ Sí |
| Necesitas acceder a atributos de la clase (cls) |	❌ No (usa @classmethod) |
| Necesitas modificar self (atributos de la instancia) |	❌ No (usa un método normal) |

## ✅ Caso práctico: Crear una fábrica de StateButton
Si tenemos ``StateButton`` (botones que cambian de color), podemos hacer una fábrica:
```py
class StateButtonFactory:
    """
    Fábrica de botones de estado que cambian de color.
    """

    @staticmethod
    def create_state_button(text):
        return StateButton(text=text)

def main(page: ft.Page):
    page.title = "Ejemplo de Factory Method con StateButton"

    # ✅ Creamos múltiples StateButtons dinámicamente
    btn1 = StateButtonFactory.create_state_button("Botón 1")
    btn2 = StateButtonFactory.create_state_button("Botón 2")
    btn3 = StateButtonFactory.create_state_button("Botón 3")

    page.add(btn1, btn2, btn3)

ft.app(target=main)

```
### 📌 Ventaja:

- No repetimos código.
- Podemos generar StateButton de forma dinámica sin instanciar la fábrica.

## 📌 Conclusión Final
- ✅ @staticmethod permite crear Factory Methods dentro de una clase sin necesidad de instanciarla.
- ✅ Facilita la reutilización del código y la organización del proyecto.
- ✅ Es útil cuando el método solo devuelve un objeto basado en parámetros sin modificar self o cls.

🚀 Ahora puedes aplicar @staticmethod para crear botones dinámicos en Flet de manera más organizada y eficiente. 🎉🔥








