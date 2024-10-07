import flet as ft
import re  # Para la validación de email

class FormField(ft.UserControl):
    def __init__(self, label: str, width: float = 200, text_size: float = 20):
        super().__init__()
        self.label = label
        self.width = width
        self.text_size = text_size
        self.text_field = ft.TextField(label=self.label, width=self.width, text_size=self.text_size)

    def get_value(self):
        """Método para obtener el valor del campo de texto"""
        return self.text_field.value

    def set_error(self, message: str):
        """Método para mostrar mensajes de error en el campo"""
        self.text_field.error_text = message
        self.update()

    def clear_error(self):
        """Método para limpiar mensajes de error"""
        self.text_field.error_text = None
        self.update()

    def build(self):
        """Construye el campo de texto"""
        return self.text_field


# Esta clase utiliza heredera de la clase formfield
# Clase que encapsula el formulario completo
class Formulario(ft.UserControl):
    def __init__(self):
        super().__init__()
        # Creamos dos campos de texto reutilizando FormField
        self.nombre_field = FormField(label="Name", width=300, text_size=18)
        self.email_field = FormField(label="Email", width=300, text_size=18)
        self.cellphone_field = FormField(label="cellphone", width=300, text_size=18)

    def validar_email(self, email: str) -> bool:
        # Validamos el email usando una expresión regular simple
        email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.match(email_regex, email) is not None
    
    def validar_phone(self, cellphone:str) -> bool:
        patron = r"^\d{10}$"
        return re.match(patron, cellphone) is not None

    def enviar_click(self, e):
        nombre = self.nombre_field.get_value()
        email = self.email_field.get_value()
        cellphone = self.cellphone_field.get_value()

        # Limpiamos los errores previos
        self.nombre_field.clear_error()
        self.email_field.clear_error()
        self.cellphone_field.clear_error()

        # Validación de los campos
        if not nombre:
            self.nombre_field.set_error("El nombre no puede estar vacío")
        if not self.validar_email(email):
            self.email_field.set_error("Email inválido")
        if not self.validar_phone(cellphone=cellphone):
            self.cellphone_field.set_error("Invalid number")

        # Si todos los campos son válidos, mostramos los valores
        if nombre and self.validar_email(email) and self.validar_phone(cellphone):
            self.page.dialog = ft.AlertDialog(title=ft.Text(f"Nombre: {nombre}\nEmail: {email} \nPhone: {cellphone}"))
            self.page.dialog.open = True
            self.page.update()

    def build(self):
        """Construye el formulario con los campos y el botón de enviar"""
        boton_enviar = ft.ElevatedButton(
            text="Enviar",
            icon=ft.icons.CHECK, 
            bgcolor=ft.colors.BLUE_500, 
            on_click=self.enviar_click)

        return ft.Column(
            controls=[
                self.nombre_field,
                self.email_field,
                self.cellphone_field,
                boton_enviar
            ]
        )



# si usamos ft.Row devolvemos una row como objeto 
# con row se construye todo en una row, (en encola en un solo renglon)
# si pasamos Ft.column se construye todo sobre una misma columna, (se apila todo en una sola columna)
# si usamos ft.Usercontrol, debemos especificar como se va construir en una funcion build()
#class Task(ft.Row):
class Task(ft.Column):
    def __init__(self, task_name: str, task_delete:callable): # pasamos una funcion, esta se pasa desde donde se instancia
        super().__init__() 
        
        self.task_name = ft.Text(task_name, visible=False)
        self.task_delete = task_delete
        self.task_edit = ft.TextField(hint_text="Enter Your Data", value=self.task_name.value)
        
        self.button_edit = ft.IconButton(icon=ft.icons.EDIT, on_click=self.clicked_edit_view, tooltip="Edit")
        self.button_save = ft.IconButton(icon=ft.icons.SAVE, on_click=self.clicked_save_view, tooltip="Save")
        self.button_delete = ft.IconButton(icon=ft.icons.DELETE, on_click=self.delete, tooltip="Delete")
        
        self.display_task = ft.Checkbox(value=False, label=self.task_name.value)
        


        self.display_view = ft.Row(
            controls=[
                self.display_task,
                ft.Row(
                    controls=[
                        self.button_edit,
                        self.button_delete
                    ]
                )
            ]
        )

        self.edit_view= ft.Row(
            controls=[
                    self.task_edit, 
                    self.button_save
                ], 
                visible=False
            )


        self.controls = [
            self.display_view,
            self.edit_view,
        ] 
    
    def clicked_edit_view(self,e):
        print("edit_view")
        self.task_edit.value = self.display_task.label
        self.display_view.visible=False
        self.edit_view.visible=True
        self.update()

    def clicked_save_view(self,e):
        print("save_view")
        self.display_task.label = self.task_edit.value
        self.display_view.visible=True
        self.edit_view.visible=False
        self.update()

    def delete(self, e):
        print("detele")
        self.task_delete(self)
    
    # si usamos usercontrol como tipo de clase
    # def build(self):
    #     return ft.Column(controls=self.controls)
    
    #obtamos por encapsular la logica, contruyendo vistas con row donde podemos hacer visible o no unobjeto Row en lugar de componente por componente
    # def edit(self, e):
    #     print("edit")
    #     self.button_edit.visible=False
    #     self.button_save.visible=True
    #     self.task_name.visible=False
    #     self.task_edit.visible=True
    #     self. update()

    # def save(self, e):
    #     print("save")
    #     self.button_edit.visible=True
    #     self.button_save.visible=False
    #     self.task_name.visible=True
    #     self.task_edit.visible=False
    #     self.task_name.value = self.task_edit.value
    #     self.update()

    



class ToDo(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="Enter Your Task", expand=True)  
        self.button_add = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked)
         # Todo se va visualizar al final en un objeto ft.column
        self.tasks_view = ft.Column() # <- dentro de este control intaciamos nuestra clase task
        
        self.controls = [
            ft.Row(
                controls=[
                    self.new_task,
                    self.button_add
                    ],
                ),
                self.tasks_view # <<<--- en esta columna se agrega la el checkboex con la tarea guardada
            ]
        

    def add_clicked(self, e):
        print("add")
        task = Task(self.new_task.value, self.task_delete)
        # agregamos los controles (las task guardada) creados a la columna append
        self.tasks_view.controls.append(task)
        # limpiamos nuestra entrada una vez salvada en la lista:  task_view 
        self.new_task.value=""
        self.update()

    def task_delete(self, task):
        self.tasks_view.controls.remove(task)
        self.update()


if __name__ == "__main__":

    def main(page: ft.Page):
        page.title = "To-Do App"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.update()

        # create application instance
        #task_1 = Task(task_name="Enter Your Data", task_delete="")
        todo = ToDo()
        # add application's root control to the page
        page.add(todo)


    ft.app(main)