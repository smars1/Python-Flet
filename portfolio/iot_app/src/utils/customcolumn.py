import flet as ft
from custombutton import CustomButton, StateButton, ButtonFactory

class CustomColumn(ft.UserControl):
    """
    Clase personalizada para orginzar elementos en columna.
    """
    def __init__(self, controls = None, spacing:int= 10, alignment= None, on_add=None, on_clear= None, on_remove=None ):
        """
        Constructor del CustomColumn.
        :param controls: Lista de controles iniciales.
        :param spacing: Espaciado entre elementos.
        :param alignment: Alineacion de los elementos en la columna.
        :param on_add: Evento que se ejecuta al agregar un elemento.
        :param on_clear: Evento que se ejecuta al limpiar la columna.
        """
        super().__init__()
        self.controls = controls if controls else []
        self.spacing = spacing
        self.alignment = alignment
        self.on_add = on_add  #  Evento al agregar un control
        self.on_remove = on_remove
        self.on_clear = on_clear  #  Evento al limpiar la columna
        #self.alignment = alignment if isinstance(alignment, ft.MainAxisAlignment) else ft.MainAxisAlignment.START
        
        self.column = None # Referencia interna a la columna
        self.view = None # Referencia a la vista interna 

    def build(self):
        """
        Construye la columna con los parametros definidos..
        """
        self.column =  ft.Column(
            controls=self.controls,
      
            spacing=self.spacing,
            alignment=self.alignment
        )
        
        # es posible agregar los botons aqui pero se manejara en la integracion
        # manejara en MainView
        # btn_add = CustomButton("add",on_click=self.add_element)

        self.view = ft.Column(
            controls=[self.column] # Agrega la columna btn_add
        )
        return self.view # Ahora `build()` devuelve la columna almacenada en `self.column`
    
    def add_element(self, e):
        """
        Agrega un nuevo texto a la columna.
        """
        new_text = ft.Text(f"Elemento {len(self.column.controls) + 1}")
        self.column.controls.append(new_text)
        self.column.update()  #  Solo actualiza la columna

    def add_control(self, control):
        """
        Agrega un nuevo control a la columna y dispara un evento opcional.
        """
        if self.column:
            self.column.controls.append(control)
            self.column.update()  #   Solo actualiza la columna

            #  Dispara el evento personalizado si esta definido
            if self.on_add:
                self.on_add(control)


    def remove_control(self, control):
        """
        Elimina un control de la columna si existe y dispara un evento opcional.
        """
        if not self.column:
            print("No se puede eliminar, la columna aun no ha sido inicializada.")
            return

        if control not in self.column.controls:
            print("El control no esta en la columna.")
            return

        # Remover control y actualizar
        self.column.controls.remove(control)
        self.column.update()

        # Dispara un evento opcional si esta definido
        if hasattr(self, "on_remove") and self.on_remove:
            self.on_remove(control)



    def clear_controls(self):
        """
        Elimina todos los controles de la columna y dispara un evento opcional.
        """
        if self.column:
            self.column.controls.clear()
            self.column.update()

            #  Dispara el evento personalizado si esta definido
            if self.on_clear:
                self.on_clear()


if __name__ == "__main__":

    def main(page: ft.Page):
        page.title = "Ejemplo de CustomColumn con Eventos"

        #   Funcion que se ejecuta cuando se agrega un nuevo elemento
        def elemento_agregado(control):
            print(f"Elemento agregado: {control.value}")

        #   Evento cuando se elimina un elemento
        def elemento_eliminado(control):
            print(f" Elemento eliminado: {control.value}")

        #   Funcion que se ejecuta cuando la columna es limpiada
        def columna_limpiada():
            print("La columna ha sido limpiada.")

        #   Crear la columna con eventos personalizados
        columna = CustomColumn(on_add=elemento_agregado, on_remove=elemento_eliminado, on_clear=columna_limpiada)

        #   Boton para agregar elementos a la columna
        def add_element(e):
            nuevo_texto = ft.Text(f"Elemento {len(columna.column.controls) + 1}")
            columna.add_control(nuevo_texto)

        #   Boton para eliminar el ultimo elemento
        def remove_element(e):
            if columna.column.controls:
                last_element = columna.column.controls[-1]
                columna.remove_control(last_element)

        #   Boton para limpiar la columna
        def clear_elements(e):
            columna.clear_controls()

        btn_add = ft.ElevatedButton("Agregar elemento", on_click=add_element)
        btn_remove = ft.ElevatedButton("Eliminar ultimo elemento", on_click=remove_element)
        btn_clear = ft.ElevatedButton("Limpiar columna", on_click=clear_elements)

        page.add(btn_add, btn_clear, columna, btn_remove)

    ft.app(target=main)
