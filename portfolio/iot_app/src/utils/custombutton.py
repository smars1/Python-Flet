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
            if self.on_click:
                self.on_click(e) # Ejecuta la funcion proporcionada
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
    

class ButtonFactory:
    """
    Clase que genera botones personalizados en Flet.
    """

    @staticmethod
    def create_button(text, color, action):
        """
        Factory Method estático para crear botones personalizados.
        :param text: Texto del boton.
        :param color: Color de fondo del boton.
        :param action: Funcion a ejecutar cuando se presiona el boton.
        :return: Un boton ElevatedButton en Flet.
        """
        return ft.ElevatedButton(
            text=text,
            bgcolor=color,
            on_click=action
        )



class StateButtonFactory:
    """
    Clase que genera botones de estado en Flet.
    """

    @staticmethod
    def create_state_button(text):
        return StateButton(text=text)








if __name__ == "__main__":
    def main(page: ft.Page):
        page.title = "Ejemplo de Botones"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.scroll = ft.ScrollMode.AUTO

        def button_click(e):
            print("¡Boton presionado!")


        # Boton Elevado
        btn1 = CustomButton(text="Aceptar", on_click=button_click, button_type="elevated")
        
        # Boton Flotante con icono
        btn2 = CustomButton(text="Añadir", icon=ft.icons.ADD, button_type="floating")

        # Boton con borde
        btn3 = CustomButton(text="Cancelar", button_type="outlined")
        
        btn4 = ButtonFactory.create_button("Aceptar", ft.colors.GREEN, lambda e: print("Aceptado"))
        btn5 = StateButtonFactory.create_state_button("Boton 5")


        # Boton que cambia de color
        btn_stateful = StateButton(text="Presioname")

        page.add(btn1, btn2, btn3, btn_stateful, btn4, btn5)



    ft.app(target=main)
