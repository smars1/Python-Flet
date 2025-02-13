import flet as ft
import re  # Para la validación de email

# si usamos ft.Row devolvemos una row como objeto 
# con row se construye todo en una row, (en encola en un solo renglon)
# si pasamos Ft.column se construye todo sobre una misma columna, (se apila todo en una sola columna)
# si usamos ft.Usercontrol, debemos especificar como se va construir en una funcion build()
#class Task(ft.Row):
class Task(ft.Column):
    def __init__(self, task_name: str, task_status_change:callable, task_delete:callable): # pasamos una funcion, esta se pasa desde donde se instancia
        super().__init__() 
        self.completed = False
        self.task_name = ft.Text(task_name, visible=False)
        self.task_delete = task_delete
        self.task_status_change = task_status_change

        self.task_edit = ft.TextField(hint_text="Enter Your Data", value=self.task_name.value)
        
        # ask controls
        self.button_edit = ft.IconButton(icon=ft.icons.EDIT, on_click=self.clicked_edit_view, tooltip="Edit")
        self.button_save = ft.IconButton(icon=ft.icons.SAVE, on_click=self.clicked_save_view, tooltip="Save")
        self.button_delete = ft.IconButton(icon=ft.icons.DELETE, on_click=self.clicked_delete_view, tooltip="Delete")
        
        self.subtask_view=ft.Column()
        self.button_add_subtask = ft.IconButton(icon=ft.icons.ADD_TASK, on_click=self.clicked_add_subtask, tooltip="Add_Subtask")
        
        
        self.display_task = ft.Checkbox(value=False, label=self.task_name.value, on_change=self.status_changed)
        
        
        
        self.display_view = ft.Row(
            controls=[
                self.display_task,
                ft.Row(
                    controls=[
                        self.button_edit,
                        self.button_delete
                    ],
                )
            ]
        )
        
        self.display_add_sub_view =ft.Row(
                controls=[
                            self.button_add_subtask,
                            ],
                        )

        self.display_sub_view = ft.Row(
                    controls=[
                        self.subtask_view,
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
            self.display_add_sub_view,
            self.display_sub_view
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

    # Podemos crear funciones que reciban como parametros otras funciones:
    # estas funciones se puden crear desde otra clase, donde se va instaciar esta clase por ejemplo
    # una vez defidas las funciones estas se pansan a la instancia
    def clicked_delete_view(self, e):
        print("detele_view")
        self.task_delete(self)

    def status_changed(self, e):
        self.completed = self.display_task.value
        self.task_status_change(self)

    # agregamos subtask
    def clicked_add_subtask(self, e):
        print("add_subtask")
        subtask = SubTask("subtask 1", subtask_delete=self.clicked_delete_subtask)
        self.subtask_view.controls.append(subtask)
        self.update()

    def clicked_delete_subtask(self, subtask):
        self.subtask_view.controls.remove(subtask)
        self.update()
    
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

class SubTask(ft.Column):
    def __init__(self, subtask_name:str, subtask_delete:callable):
        super().__init__()
        self.get_subtask_name = ft.Text(value=subtask_name)
        self.get_subtask_time = ft.Text()
        self.subtask_delete = subtask_delete

        self.set_subtask_time = ft.TextField(hint_text="Time", label="Subtask")
        self.set_subtask_name = ft.TextField(value=self.get_subtask_name.value,  hint_text="Enter Your SubTask", label="Subtask")

        self.button_save_subtask = ft.IconButton(icon=ft.icons.TASK, on_click=self.clicked_save_subtask, tooltip="Save_Subtask")
        self.button_edit_subtask = ft.IconButton(icon=ft.icons.EDIT_NOTE, on_click=self.cliked_edit_subtask, tooltip="Edit_Subtask" )
        self.button_delete_subtask = ft.IconButton(icon=ft.icons.DELETE, on_click=self.clicked_delete_subtask, tooltip="Delete_Subtask")

        
        # a los controles solo se pasan compoenentes no valores como self.button_save_subtask.value si no el componente completo: self.button_save_subtask
        
        #setters
        self.display_edit = ft.Row(
            controls=[
                self.set_subtask_name,
                self.set_subtask_time,
                self.button_save_subtask
            ]
        )

        #getters
        self.display_view = ft.Row(
            controls=[
                self.get_subtask_name,
                self.get_subtask_time,
                self.button_edit_subtask,
                self.button_delete_subtask

            ],
            visible=False
        )
 
        self.controls = [self.display_edit, self.display_view]

    def clicked_save_subtask(self, e):
        print("Save_subtask")
        self.get_subtask_name.value = self.set_subtask_name.value
        self.get_subtask_time.value = self.set_subtask_time.value

        self.display_edit.visible=False
        self.display_view.visible=True

        self.set_subtask_name.value = ""
        self.set_subtask_time.value = ""
        self.update()

    def cliked_edit_subtask(self, e):
        print("Edit_subtask")
        self.display_view.visible=False
        self.display_edit.visible = True

        self.set_subtask_name.value = self.get_subtask_name.value
        self.set_subtask_time.value = self.get_subtask_time.value
        self.update()


    def clicked_delete_subtask(self, e):
        print("Delete_Subtask")
        self.subtask_delete(self)

        







class ToDo(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="Enter Your Task", expand=True)  
        self.button_add = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked)
         # Todo se va visualizar al final en un objeto ft.column
        self.tasks_view = ft.Column() # <- dentro de este control intaciamos nuestra clase task
        
        self.filter = ft.Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                ft.Tab(text="All"),
                ft.Tab(text="Active"),
                ft.Tab(text="Completed"),
                ]
            
        )



        self.controls = [
            ft.Row(
                controls=[
                    self.new_task,
                    self.button_add
                    ],
                ),
                ft.Column(
                    controls=[
                    self.filter,
                    self.tasks_view # <<<--- en esta columna se agrega la el checkboex con la tarea guardada 
                    ]
                )
            ]
        
       
        
    def before_update(self):
        # desglosamos el index para movernos al text correspondiente y tomar su string
        #status = self.filter.tabs[self.filter.selected_index].text
        status = self.filter.tabs[self.filter.selected_index].text.lower()  # Obtener la pestaña seleccionada en minúsculas
        for task in self.tasks_view.controls:
            task.visible = (
                status == "all"
                or (status == "active" and task.completed == False)
                or (status == "completed" and task.completed)
            )

    
    def tabs_changed(self, e):
        print("tab_changed")  
        self.update()  

    def task_status_change(self, e):
        print("Status_Change")
        self.update()

    def add_clicked(self, e):
        print("add")
        task = Task(self.new_task.value, self.task_status_change, self.task_delete)
        # agregamos los controles (las task guardada) creados a la columna el metodo .controls admite elemetos de lista con append
        self.tasks_view.controls.append(task)
        # limpiamos nuestra entrada una vez salvada en la lista:  task_view 
        self.new_task.value=""
        self.update()

    def task_delete(self, task):
        self.tasks_view.controls.remove(task)
        self.update()


# Clase que funciona como contenedor
class ContainerClass(ft.UserControl):
    def __init__(self, child):
        super().__init__()
        self.child = child

    def build(self):
        # Encapsulando la clase `MiClase` en un `Container`
        return ft.Container(
            content=self.child,
            padding=20,
            border_radius=10,
            bgcolor=ft.colors.BLACK87,
            adaptive=True
        )




if __name__ == "__main__":

    def main(page: ft.Page):
        page.title = "To-Do App"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.scroll = ft.ScrollMode.AUTO
        page.update()
        
        # create application instance
        #task_1 = Task(task_name="Enter Your Data", task_delete="")
        todo = ToDo()
        container = ContainerClass(todo)

        #subtask = SubTask("subtask 1")
        # add application's root control to the page
        page.add(container)


    ft.app(main)