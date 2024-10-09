import flet as ft
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO
    df = None

    def file_picker_result(e: ft.FilePickerResultEvent):
        nonlocal df
        if e.files:
            file_path = e.files[0].path
            df = pd.read_csv(file_path, sep=None, engine='python', encoding='latin1', on_bad_lines='skip')
            update_dataframe_view(df)

    def update_dataframe_view(dataframe: pd.DataFrame):
        table = ft.DataTable(
            columns=[ft.DataColumn(ft.Text(col)) for col in dataframe.columns],
            rows=[
                ft.DataRow(
                    cells=[ft.DataCell(ft.Text(str(dataframe.iloc[i, j]))) for j in range(dataframe.shape[1])]
                ) for i in range(dataframe.shape[0])
            ]
        )

        scrollable_column = ft.Column(
            controls=[table],
            scroll=ft.ScrollMode.AUTO,  # Habilita el desplazamiento
            expand=True  # Permite expandirse para usar todo el espacio disponible
        )

        scrollable_row=ft.Row(controls=[scrollable_column], scroll=ft.ScrollMode.AUTO,expand=True)


        page.controls.clear()
        page.add(file_picker_button, file_info, scrollable_row, btn_remove_nulls, btn_remove_duplicates, btn_normalize, btn_encode, btn_export_csv)
        page.update()

    def remove_nulls(e):
        nonlocal df
        if df is not None:
            df = df.dropna()
            update_dataframe_view(df)

    def remove_duplicates(e):
        nonlocal df
        if df is not None:
            df = df.drop_duplicates()
            update_dataframe_view(df)

    def normalize_data(e):
        nonlocal df
        if df is not None:
            numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
            scaler = StandardScaler()
            df[numerical_columns] = scaler.fit_transform(df[numerical_columns])
            update_dataframe_view(df)

    def encode_categorical(e):
        nonlocal df
        if df is not None:
            categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
            encoder = LabelEncoder()
            for col in categorical_columns:
                df[col] = encoder.fit_transform(df[col])
            update_dataframe_view(df)

    def export_data(e):
        if df is not None:
            df.to_csv("datos_procesados.csv", index=False)
            file_info.value = "Datos exportados a 'datos_procesados.csv'."
            page.update()


    btn_remove_nulls = ft.ElevatedButton("Eliminar Nulos", on_click=remove_nulls)
    btn_remove_duplicates = ft.ElevatedButton("Eliminar Duplicados", on_click=remove_duplicates)
    btn_normalize = ft.ElevatedButton("Normalizar Datos", on_click=normalize_data)
    btn_encode = ft.ElevatedButton("Codificar Categóricos", on_click=encode_categorical)
    btn_export_csv = ft.ElevatedButton("Exportar CSV", on_click=export_data)
    
    file_picker = ft.FilePicker(on_result=file_picker_result)
    file_picker_button = ft.ElevatedButton("Seleccionar Archivo", on_click=lambda _: file_picker.pick_files())

    file_info = ft.Text()
    

    page.add(file_picker_button, file_info)
    page.overlay.append(file_picker)
    page.update()

ft.app(target=main)
