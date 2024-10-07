import flet as ft
from utils.formfield import ToDo

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