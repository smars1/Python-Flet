import flet as ft
class CustomTextField(ft.UserControl):
    """
    Clase personalizada para entradas de texto en Flet.
    Permite reutilizar estilos y agregar validaciones.
    """

    def __init__(self, label:str ="", hint_text:str ="", on_change:callable =None, password:bool =False, width:int=300):
        super().__init__()
        self.label = label
        self.hint_text = hint_text
        self.on_change = on_change
        self.password = password
        self.width = width
        self.new_text = None # Elimina esta línea, ya que el TextField se define en build()

    # ✅ Evento para capturar texto en tiempo real
    def on_text_change(self, e):
        print(f"Texto ingresado: {e.control.value}")
        if self.on_change:
            self.on_change(e) # Ejecuta la funcion proporcionada
        self.update()

    def build(self):
        """
        Construye el TextField con los parametros definidos
        """
        self.new_text =  ft.TextField(
            label=self.label,
            hint_text=self.hint_text,
            width=self.width,
            password=self.password,  # ✅ Soporta contraseñas
            on_change=self.on_text_change  # ✅ Permite pasar funciones dinamicas
        )
        return self.new_text
    
if __name__ == "__main__":

    def main(page: ft.Page):
        page.title = "Ejemplo de CustomTextField"
        
        # ✅ Crear varias entradas reutilizando `CustomTextField`
        name_input = CustomTextField(label="Nombre", hint_text="Ingresa tu nombre")
        email_input = CustomTextField(label="Correo", hint_text="Ingresa tu correo")
        password_input = CustomTextField(label="Contraseña", password=True, hint_text="Ingresa tu contraseña")

        page.add(name_input, email_input, password_input)

ft.app(target=main)








