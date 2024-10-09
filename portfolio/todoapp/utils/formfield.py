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
    
if __name__ == "__main__":

    def main(page: ft.Page):
        page.title = "To-Do App"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.update()

        # create application instance
        #task_1 = Task(task_name="Enter Your Data", task_delete="")
        todo = Formulario()
        # add application's root control to the page
        page.add(todo)


    ft.app(main)