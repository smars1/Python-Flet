import flet as ft
import boto3
import os
from dotenv import load_dotenv

# Cargar variables de entorno (asegúrate de tener un .env con las credenciales)
load_dotenv()
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

# Inicializar cliente de S3
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

def main(page: ft.Page):
    page.title = "Subir archivos a S3"
    page.window_width = 500
    page.window_height = 400
    
    bucket_name_input = ft.TextField(label="Nombre del Bucket", width=400)
    folder_name_input = ft.TextField(label="Nombre de la Subcarpeta (opcional)", width=400)
    
    def subir_archivo(e: ft.FilePickerResultEvent):
        if e.files and bucket_name_input.value:
            archivo_local = e.files[0].path
            nombre_en_s3 = os.path.basename(archivo_local)
            bucket_name = bucket_name_input.value
            subcarpeta = folder_name_input.value.strip()
            
            # Si se especifica una subcarpeta, agregarla al nombre del archivo
            if subcarpeta:
                nombre_en_s3 = f"{subcarpeta}/{nombre_en_s3}"
            
            try:
                s3_client.upload_file(archivo_local, bucket_name, nombre_en_s3)
                resultado.value = f"Archivo subido exitosamente a {bucket_name}/{nombre_en_s3}"
            except Exception as ex:
                resultado.value = f"Error al subir: {ex}"
            page.update()
    
    file_picker = ft.FilePicker(on_result=subir_archivo)
    page.overlay.append(file_picker)
    
    btn_subir = ft.ElevatedButton("Seleccionar archivo", on_click=lambda _: file_picker.pick_files(allow_multiple=False))
    resultado = ft.Text("Selecciona un archivo, especifica un bucket y opcionalmente una subcarpeta para subir a S3")
    
    page.add(bucket_name_input, folder_name_input, btn_subir, resultado)

ft.app(target=main)
