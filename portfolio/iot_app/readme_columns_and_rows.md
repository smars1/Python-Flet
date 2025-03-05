# 📌 ¿Por qué crear clases para Column y Row?
- ✅ Código más limpio y organizado → Evita escribir muchas líneas repetitivas.
- ✅ Mejor reutilización → Puedes usar la misma clase en diferentes partes de la app sin repetir código.
- ✅ Facilita la personalización → Puedes agregar opciones de configuración, eventos o estilos.
- ✅ Más control sobre la UI → Permite manejar alineación, espaciado y otros estilos de manera centralizada.

### ✅ Crear una clase para Column (Lista de elementos)
📌 Ejemplo: CustomColumn que agrupa elementos de forma ordenada
```py
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

```
📌 Ventajas:

Ahora puedes crear columnas sin repetir código.
Puedes definir la alineación y el espaciado una sola vez.
Fácil de personalizar en otros proyectos.

### ✅ Crear una clase para Row (Elementos en línea horizontal)
📌 Ejemplo: CustomRow para organizar elementos horizontalmente
```py
import flet as ft

class CustomRow(ft.UserControl):
    """
    Clase personalizada para organizar elementos en una fila con referencia interna.
    """

    def __init__(self, controls=None, spacing=10, alignment=None):
        super().__init__()
        self.controls = controls if controls else []
        self.spacing = spacing
        self.alignment = alignment
        self.row = None  # 🔹 Referencia interna a la fila

    def build(self):
        """
        Construye la fila y guarda la referencia.
        """
        self.row = ft.Row(
            controls=self.controls,
            spacing=self.spacing,
            alignment=self.alignment
        )
        return self.row  # 🔹 Retornamos la fila guardada en `self.row`

    def add_control(self, control):
        """
        Agrega un nuevo control a la fila.
        """
        self.row.controls.append(control)
        self.row.update()  # 🔹 Solo actualiza la fila

    def remove_control(self, control):
        """
        Elimina un control de la fila si existe.
        """
        if control in self.row.controls:
            self.row.controls.remove(control)
            self.row.update()

    def clear_controls(self):
        """
        Elimina todos los controles de la fila.
        """
        self.row.controls.clear()
        self.row.update()


if __name__ == "__main__":
    def main(page: ft.Page):
        page.title = "Ejemplo de CustomRow con referencia interna"

        # Crear una fila vacía
        fila = CustomRow()

        # Botón para agregar elementos a la fila
        def add_element(e):
            fila.add_control(ft.Text("Nuevo elemento agregado"))

        # Botón para limpiar la fila
        def clear_elements(e):
            fila.clear_controls()

        btn_add = ft.ElevatedButton("Agregar elemento", on_click=add_element)
        btn_clear = ft.ElevatedButton("Limpiar fila", on_click=clear_elements)

        page.add(btn_add, btn_clear, fila)

    ft.app(target=main)


```
📌 Ventajas:

Permite organizar elementos en horizontal sin escribir Row cada vez.
Es más fácil agregar alineación y espaciado sin repetir código.
Útil para menús de navegación, listas horizontales o barras de botones.

## 📌 ¿Cuándo usar CustomColumn o CustomRow?

| Caso de uso |	Usa CustomColumn | Usa CustomRow |
| ---- |---- | ---- |
| Lista de elementos apilados verticalmente | ✅ Sí | ❌ No |
| Menú de navegación |	❌ No | ✅ Sí |
| Botones alineados en una barra |	❌ No | ✅ Sí |
| Formularios con múltiples campos | ✅ Sí |	❌ No |
| Encabezados con logo y botones | ❌ No	| ✅ Sí |

### 📌 Resumen final
- ✅ Crear clases para Column y Row es una buena práctica cuando quieres organizar mejor tu UI y hacerla más reutilizable.
- ✅ CustomColumn y CustomRow permiten crear estructuras sin repetir código y con mayor control sobre alineación y espaciado.
- ✅ Se pueden personalizar fácilmente y hacer más escalables grandes aplicaciones en Flet.

- ✅ Modificar dinámicamente los elementos sin necesidad de reconstruir el control completo.
- ✅ Agregar o quitar elementos en tiempo real sin necesidad de llamar a self.update() sobre todo el UserControl.
- ✅ Mejor control sobre los datos y estados internos de la columna o fila.


## 📌 Notas finales
- ✅ Es una mejor práctica inicializar una referencia (self.column o self.row) en lugar de solo retornarlas en build().
- ✅ Permite modificar los elementos sin necesidad de reconstruir todo el UserControl.
- ✅ Las funciones add_control(), remove_control(), y clear_controls() hacen que la UI sea más flexible.
- ✅ Se puede aplicar tanto para Column como para Row de manera eficiente.

💡 Con este enfoque, ahora puedes construir interfaces más dinámicas y eficientes en Flet! 🚀🔥

💡 Ahora puedes organizar tu UI en Flet de manera más estructurada y profesional! 🚀🔥