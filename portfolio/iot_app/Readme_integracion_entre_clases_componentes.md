# 📌 ¿Cómo integrar CustomButton con CustomColumn correctamente?
### 🔹 Objetivo:
- Crear botones personalizados (CustomButton) dentro de CustomColumn.
- Los botones deben interactuar con la columna (Agregar, Eliminar, Limpiar).
- Manejar eventos directamente en CustomButton, sin definir eventos en main().

### ✅ 1. Modificamos CustomButton para soportar eventos dinámicos
Actualmente, tenemos CustomButton, pero los eventos (on_click) se definen en main().
Lo mejor es permitir que CustomButton reciba eventos dinámicos para interactuar con CustomColumn.

```py
import flet as ft

class CustomButton(ft.UserControl):
    """
    Botón personalizado reutilizable en Flet.
    """

    def __init__(self, text: str, on_click=None, bgcolor=ft.colors.BLUE_500, text_color=ft.colors.WHITE):
        super().__init__()
        self.text = text
        self.bgcolor = bgcolor
        self.text_color = text_color
        self.on_click = on_click  # ✅ Evento dinámico para clic

    def build(self):
        """
        Construye el botón con las propiedades definidas.
        """
        return ft.ElevatedButton(
            text=self.text,
            bgcolor=self.bgcolor,
            color=self.text_color,
            on_click=self.on_click  # ✅ Usa el evento dinámico
        )

```
✅ Ahora CustomButton acepta una función on_click dinámica, lo que nos permite conectarlo fácilmente con CustomColumn.

## ✅ 2. Integramos CustomButton con CustomColumn
Ahora modificamos CustomColumn para manejar CustomButton como parte de su estructura.

```py
class CustomColumn(ft.UserControl):
    """
    Clase personalizada para organizar elementos en una columna con botones dinámicos.
    """

    def __init__(self, controls=None, spacing=10, alignment=ft.MainAxisAlignment.START):
        super().__init__()
        self.controls = controls if controls else []
        self.spacing = spacing
        self.alignment = alignment
        self.column = None  # Referencia a la columna interna

    def build(self):
        """
        Construye la columna y agrega botones para interactuar con ella.
        """
        self.column = ft.Column(
            controls=self.controls,
            spacing=self.spacing,
            alignment=self.alignment
        )

        # ✅ Creamos botones usando `CustomButton`
        btn_add = CustomButton("Agregar", on_click=self.add_element, bgcolor=ft.colors.GREEN_500)
        btn_remove = CustomButton("Eliminar último", on_click=self.remove_element, bgcolor=ft.colors.RED_500)
        btn_clear = CustomButton("Limpiar columna", on_click=self.clear_elements, bgcolor=ft.colors.ORANGE_500)

        # ✅ Retornamos la estructura completa
        return ft.Column([
            btn_add, btn_remove, btn_clear,  # 🔹 Botones dentro de la UI
            self.column  # 🔹 Columna donde se agregan elementos dinámicamente
        ])

    def add_element(self, e):
        """
        Agrega un nuevo texto a la columna.
        """
        new_text = ft.Text(f"Elemento {len(self.column.controls) + 1}")
        self.column.controls.append(new_text)
        self.column.update()  # 🔹 Solo actualiza la columna

    def remove_element(self, e):
        """
        Elimina el último elemento de la columna.
        """
        if self.column.controls:
            self.column.controls.pop()
            self.column.update()

    def clear_elements(self, e):
        """
        Elimina todos los elementos de la columna.
        """
        self.column.controls.clear()
        self.column.update()

```
### ✅ 3. main() ahora es mucho más limpio
Como los botones ya están dentro de CustomColumn, en main() solo creamos la columna:
```py
def main(page: ft.Page):
    page.title = "Ejemplo de Integración entre CustomButton y CustomColumn"

    # ✅ Solo agregamos `CustomColumn`, ya incluye botones y lógica
    columna = CustomColumn()

    page.add(columna)

ft.app(target=main)
```

📌 ¿Por qué esta integración es mejor?
- ✅ CustomColumn ahora gestiona sus propios botones → No dependemos de main() para definir eventos.
- ✅ Separamos la lógica de UI → CustomButton sigue siendo reutilizable y flexible.
- ✅ El código es más limpio y fácil de mantener.

## 🚀 Resultado esperado
- 🔹 Ahora CustomColumn tiene 3 botones funcionales dentro de sí misma:
- "Agregar" → Añade un nuevo Text() dentro de la columna.
- "Eliminar último" → Elimina el último elemento agregado.
-"Limpiar columna" → Borra todos los elementos.

💡 Ya no es necesario definir eventos en main(), todo se maneja dentro de CustomColumn. 🚀🔥

# 📌 ¿Cómo guardar una vista en lugar de retornar el componente directamente?
Ahora vamos a mejorar CustomColumn para que almacene su vista en self.view, en lugar de retornarla directamente en build().

Una mejor práctica guardar la vista (self.view) en lugar de retornarla directamente en build(), ya que permite:

- ✅ Mantener una referencia interna del componente, lo que facilita modificaciones sin necesidad de reconstruir todo el UserControl.
- ✅ Modificar dinámicamente la UI sin necesidad de llamar build() nuevamente.
- ✅ Reducir re-renderizados innecesarios, lo que mejora el rendimiento.

```py
import flet as ft

class CustomColumn(ft.UserControl):
    """
    Clase personalizada para organizar elementos en una columna con botones dinámicos.
    """

    def __init__(self, controls=None, spacing=10, alignment=ft.MainAxisAlignment.START):
        super().__init__()
        self.controls = controls if controls else []
        self.spacing = spacing
        self.alignment = alignment
        self.view = None  # 🔹 Guardamos la vista en una variable interna
        self.column = None  # 🔹 Referencia a la columna interna

    def build(self):
        """
        Construye la columna y almacena la vista para modificarla dinámicamente.
        """
        self.column = ft.Column(
            controls=self.controls,
            spacing=self.spacing,
            alignment=self.alignment
        )

        # ✅ Creamos botones usando `CustomButton`
        btn_add = CustomButton("Agregar", on_click=self.add_element, bgcolor=ft.colors.GREEN_500)
        btn_remove = CustomButton("Eliminar último", on_click=self.remove_element, bgcolor=ft.colors.RED_500)
        btn_clear = CustomButton("Limpiar columna", on_click=self.clear_elements, bgcolor=ft.colors.ORANGE_500)

        # 🔹 Guardamos la vista para referencia futura
        self.view = ft.Column([
            btn_add, btn_remove, btn_clear,  # 🔹 Botones dentro de la UI
            self.column  # 🔹 Columna donde se agregan elementos dinámicamente
        ])
        
        return self.view  # 🔹 Retornamos la vista almacenada en `self.view`

    def add_element(self, e):
        """
        Agrega un nuevo texto a la columna.
        """
        new_text = ft.Text(f"Elemento {len(self.column.controls) + 1}")
        self.column.controls.append(new_text)
        self.column.update()  # 🔹 Solo actualiza la columna

    def remove_element(self, e):
        """
        Elimina el último elemento de la columna.
        """
        if self.column.controls:
            self.column.controls.pop()
            self.column.update()

    def clear_elements(self, e):
        """
        Elimina todos los elementos de la columna.
        """
        self.column.controls.clear()
        self.column.update()

```

### ✅ Ventajas de almacenar la vista en self.view
- 1️⃣ Permite modificar la vista sin necesidad de llamar build() otra vez.
- 2️⃣ Facilita el acceso a la UI desde métodos internos (add_element(), remove_element(), etc.).
- 3️⃣ Evita recrear la vista en cada update(), mejorando la eficiencia.

### ✅ ¿Cómo usar CustomColumn en main()?
La lógica sigue siendo igual, pero ahora la estructura es más organizada y escalable.

```py
def main(page: ft.Page):
    page.title = "Ejemplo de CustomColumn con referencia interna"

    # ✅ Solo agregamos `CustomColumn`, ya incluye botones y lógica
    columna = CustomColumn()

    page.add(columna)

ft.app(target=main)

```

## 📌 🚀 Resumen
| ❌ Antes (Retornando directamente Column())|	✅ Ahora (Guardando self.view)|
| ---- | ---- |
| Se crea una nueva Column() cada vez que se llama build().|	self.view almacena la vista y no se vuelve a crear innecesariamente.|
| No hay referencia interna, por lo que hay que llamar update() a toda la UI.|	Se puede actualizar solo la parte necesaria sin reconstruir todo el UserControl.|
| Difícil modificar dinámicamente la UI sin reconstruirla.|	self.view permite modificar elementos de manera eficiente.|

💡 Ahora CustomColumn es más escalable y eficiente, permitiendo modificaciones sin necesidad de reconstruir toda la UI! 🚀🔥


