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


# ✅ Solución mejorada para remove_control()
### 📌 Código corregido y optimizado
```py
def remove_control(self, control):
    """
    Elimina un control de la columna si existe y dispara un evento opcional.
    """
    if not self.column:
        print("⚠️ No se puede eliminar, la columna aún no ha sido inicializada.")
        return

    if control not in self.column.controls:
        print("⚠️ El control no está en la columna.")
        return

    # ✅ Remover control y actualizar
    self.column.controls.remove(control)
    self.column.update()

    # ✅ Dispara un evento opcional si está definido
    if hasattr(self, "on_remove") and self.on_remove:
        self.on_remove(control)

```

## ✅ Mejoras aplicadas

| 🔹 Problema anterior | ✅ Solución aplicada |
| ------------------ | -------------------- | 
| No verifica si self.column está inicializado|	Ahora verifica if not self.column: antes de acceder a .controls.|
| No verifica si el control existe antes de removerlo|	Se agrega if control not in self.column.controls: para evitar errores.|
| No dispara un evento cuando se elimina un control|	Se agrega on_remove para permitir eventos personalizados.|


## ✅ Uso mejorado con eventos (on_add, on_remove, on_clear)
Ahora podemos agregar eventos cuando un control se agrega, elimina o limpia en CustomColumn.

```py
import flet as ft

class CustomColumn(ft.UserControl):
    """
    Clase personalizada para organizar elementos en una columna con eventos dinámicos.
    """

    def __init__(self, controls=None, spacing=10, alignment=None, 
                 on_add=None, on_remove=None, on_clear=None):
        """
        Constructor del CustomColumn.
        :param controls: Lista de controles iniciales.
        :param spacing: Espaciado entre elementos.
        :param alignment: Alineación de los elementos en la columna.
        :param on_add: Evento al agregar un elemento.
        :param on_remove: Evento al eliminar un elemento.
        :param on_clear: Evento al limpiar la columna.
        """
        super().__init__()
        self.controls = controls if controls else []
        self.spacing = spacing
        self.alignment = alignment
        self.on_add = on_add  # 🔹 Evento al agregar
        self.on_remove = on_remove  # 🔹 Evento al eliminar
        self.on_clear = on_clear  # 🔹 Evento al limpiar
        self.column = None  # 🔹 Referencia interna a la columna

    def build(self):
        """
        Construye la columna con los parámetros definidos.
        """
        self.column = ft.Column(
            controls=self.controls,
            spacing=self.spacing,
            alignment=self.alignment
        )
        return self.column  # ✅ Retornamos la columna guardada en `self.column`

    def add_control(self, control):
        """
        Agrega un nuevo control a la columna y dispara un evento opcional.
        """
        if self.column:
            self.column.controls.append(control)
            self.column.update()  # ✅ Solo actualiza la columna

            if self.on_add:
                self.on_add(control)  # 🔹 Dispara evento si está definido

    def remove_control(self, control):
        """
        Elimina un control de la columna si existe y dispara un evento opcional.
        """
        if not self.column:
            print("⚠️ No se puede eliminar, la columna aún no ha sido inicializada.")
            return

        if control not in self.column.controls:
            print("⚠️ El control no está en la columna.")
            return

        self.column.controls.remove(control)
        self.column.update()

        if self.on_remove:
            self.on_remove(control)  # 🔹 Dispara evento si está definido

    def clear_controls(self):
        """
        Elimina todos los controles de la columna y dispara un evento opcional.
        """
        if self.column:
            self.column.controls.clear()
            self.column.update()

            if self.on_clear:
                self.on_clear()  # 🔹 Dispara evento si está definido

```

## ✅ Uso con eventos (on_add, on_remove, on_clear)
Ahora podemos manejar eventos personalizados cuando agregamos, eliminamos o limpiamos la columna.

```
def main(page: ft.Page):
    page.title = "Ejemplo de CustomColumn con Eventos"

    # ✅ Evento cuando se agrega un nuevo elemento
    def elemento_agregado(control):
        print(f"✅ Elemento agregado: {control.value}")

    # ✅ Evento cuando se elimina un elemento
    def elemento_eliminado(control):
        print(f"❌ Elemento eliminado: {control.value}")

    # ✅ Evento cuando la columna se limpia
    def columna_limpiada():
        print("🗑️ La columna ha sido limpiada.")

    # ✅ Crear la columna con eventos
    columna = CustomColumn(on_add=elemento_agregado, on_remove=elemento_eliminado, on_clear=columna_limpiada)

    # ✅ Botón para agregar elementos
    def add_element(e):
        nuevo_texto = ft.Text(f"Elemento {len(columna.column.controls) + 1}")
        columna.add_control(nuevo_texto)

    # ✅ Botón para eliminar el último elemento
    def remove_element(e):
        if columna.column.controls:
            last_element = columna.column.controls[-1]
            columna.remove_control(last_element)

    # ✅ Botón para limpiar la columna
    def clear_elements(e):
        columna.clear_controls()

    btn_add = ft.ElevatedButton("Agregar elemento", on_click=add_element)
    btn_remove = ft.ElevatedButton("Eliminar último elemento", on_click=remove_element)
    btn_clear = ft.ElevatedButton("Limpiar columna", on_click=clear_elements)

    page.add(btn_add, btn_remove, btn_clear, columna)

ft.app(target=main)

```

## 📌 Explicación detallada
| 🔹 Mejoras aplicadas | 📌 Cómo se implementaron |
| -------------------- | ------------------------- | 
| Evita errores al eliminar controles|	Se agregaron validaciones if not self.column: y if control not in self.column.controls:.|
| Se pueden manejar eventos personalizados|	on_add, on_remove, on_clear permiten ejecutar funciones externas al modificar la columna.|
| Evita lambda dentro de build()|	Los eventos (add_control(), remove_control(), clear_controls()) están bien organizados.|
| UI más eficiente|	Solo se actualiza la Column sin reconstruir todo el UserControl.|