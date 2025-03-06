# 📌 ¿Por qué usar Container?
- ✅ Mejor organización visual → Permite manejar márgenes, bordes y fondo.
- ✅ Mejor control de diseño → Se puede definir ancho, alto y alineación fácilmente.
- ✅ Facilita la reutilización → Se pueden aplicar estilos globales sin afectar la lógica interna de CustomColumn.
### # ✅ Agregando Container a CustomColumn


## 📌 Explicación completa de CustomContainer
### 1️⃣ CustomContainer hereda de ``ft.UserControl``

```py
class CustomContainer(ft.UserControl):
```

### 📌 ft.UserControl es una clase base en Flet que permite crear componentes personalizados.

- Nos permite encapsular la lógica del Container en un solo lugar.
- Nos da acceso a métodos como build() y update() para manejar la UI dinámicamente.

### 2️⃣ Constructor __init__()

```py
def __init__(self, content=None, width=400, height=400, padding=20, bgcolor=ft.colors.BLUE_GREY_50, border_radius=10, alignment=ft.alignment.center):
    super().__init__()
    self.content = content if content else ft.Column()  
    self.width = width
    self.height = height
    self.padding = padding
    self.bgcolor = bgcolor
    self.border_radius = border_radius
    self.alignment = alignment

```
### 📌 El constructor inicializa las propiedades del contenedor.

|Parámetro |	Propósito|
| ---- | ---- |
|content |	Define qué elementos estarán dentro del contenedor. Si no se pasa nada, se usa un ft.Column(). |
| width y height |	Define el tamaño del contenedor (400x400 por defecto). |
| padding |	Agrega espacio dentro del contenedor. |
| bgcolor |	Define el color de fondo del contenedor. | 
| border_radius |	Redondea las esquinas del contenedor. | 
| alignment |	Alinea el contenido dentro del contenedor (por defecto está centrado). |

### 3️⃣ Método build() 
```py
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
        alignment=self.alignment
    )
    return self.container  

```
### 📌 Este método se ejecuta automáticamente cuando Flet renderiza el componente.
- ✅ Crea un Container con los parámetros que pasamos en __init__().
- ✅ Devuelve self.container para que Flet lo muestre en la pantalla.

### 4️⃣ Método update_content()
```py
def update_content(self, new_content):
    """
    Permite actualizar el contenido dinámicamente.
    """
    if self.container:
        self.container.content = new_content  
        self.container.update()  
        self.update()  

```
### 📌 Este método permite cambiar el contenido del CustomContainer en tiempo de ejecución.
- ✅ self.container.content = new_content → Reemplaza el contenido del contenedor.
- ✅ self.container.update() → Actualiza el Container para que Flet muestre los cambios.
- ✅ self.update() → Actualiza el UserControl completo en caso de que sea necesario.

## 📌 Explicación del código de prueba
Ahora analizaremos cómo se usa CustomContainer en la prueba dentro de main().

### 1️⃣ main() configura la página
```py
def main(page: ft.Page):
    page.title = "Prueba de CustomContainer"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  #  Centramos todo

```
- ✅ Se define el título de la ventana y se centran todos los elementos en la pantalla.
- ✅ horizontal_alignment y vertical_alignment aseguran que los elementos aparezcan bien

### 2️⃣ Creamos CustomColumn
```py
custom_column = CustomColumn()
```
### 📌 CustomColumn es una columna personalizada que podemos llenar con elementos dinámicos.
✅ Se usará dentro de CustomContainer para contener elementos.

### 3️⃣ Creamos un botón para agregar elementos a CustomColumn
```py
btn_add = CustomButton("Agregar", on_click=custom_column.add_element, bgcolor=ft.colors.GREEN_500)
```
- ✅ Botón "Agregar" que, cuando se presiona, llama a custom_column.add_element().
- ✅ El color del botón es GREEN_500 para destacarlo visualmente.

### 4️⃣ Creamos CustomContainer con CustomColumn y CustomButton adentro
```py
custom_container = CustomContainer(
    content=ft.Column([btn_add, custom_column]),  
    width=500,
    height=500,
    bgcolor=ft.colors.WHITE,
    padding=30,
    border_radius=15
)

```
### 📌 Aquí combinamos CustomContainer con CustomColumn y el botón.
- ✅ ft.Column([btn_add, custom_column]) → Agrupa los elementos dentro del Container.
- ✅ width=500, height=500 → Hace que el contenedor sea más grande.
- ✅ bgcolor=ft.colors.WHITE → Se usa un fondo blanco para mayor visibilidad.
- ✅ padding=30 → Agrega margen interno para que no esté pegado a los bordes.
- ✅ border_radius=15 → Bordes redondeados.

### 5️⃣ Creamos otro CustomContainer vacío con color naranja
```py
container = CustomContainer(bgcolor=ft.colors.ORANGE_50)
```
- ✅ Este CustomContainer es un segundo contenedor vacío solo para probar que se puede agregar otro elemento.
- ✅ Tiene color ORANGE_50 para diferenciarlo del primer contenedor.
```
page.add(custom_container, container)
```
### 📌 Finalmente, agregamos ambos contenedores a la página para que se muestren en la UI.
- ✅ custom_container → Contiene la columna y el botón.
- ✅ container → Es un CustomContainer vacío con color naranja.

## 📌 🚀 Resumen Final
| Concepto	| Explicación |
| ---- | ---- | 
| CustomContainer |	Es una clase personalizada basada en ft.UserControl para organizar la UI.|
| build() |	Crea el Container con las propiedades configuradas.|
| update_content(new_content) |	Permite actualizar dinámicamente el contenido del contenedor.|
| main() |	Crea una prueba donde CustomContainer contiene una columna y un botón.|
| page.add(custom_container, container) |	Agrega dos contenedores a la pantalla para visualización|

## 📌 🚀 Ahora puedes replicar CustomContainer en otros proyectos
- ✅ Puedes usar CustomContainer para organizar otros componentes como CustomTextField, CustomRow, etc.
- ✅ Puedes modificar update_content() para actualizarlo con diferentes elementos dinámicamente.
- ✅ Puedes cambiar el bgcolor, padding, width y otros atributos para personalizarlo.

💡 ¡Ahora entiendes completamente CustomContainer y puedes usarlo en cualquier proyecto Flet! 🚀🔥







