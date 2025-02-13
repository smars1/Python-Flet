# ESP32 IoT Dashboard con AWS Lambda, API Gateway y DynamoDB

## Descripción del Proyecto
Este proyecto permite la integración de un **ESP32** con AWS para recopilar datos de sensores y visualizarlos en una aplicación desarrollada con **Flet**. Utiliza **AWS Lambda** para procesar los datos, **API Gateway** para exponer una API REST y **DynamoDB** como base de datos para almacenar los registros.

## Arquitectura del Proyecto
1. **ESP32** envía datos de sensores mediante MQTT a **AWS IoT Core**.
2. AWS IoT Core publica los datos en una **Lambda Function** que guarda los registros en **DynamoDB**.
3. API Gateway expone una API REST que permite consultar estos datos.
4. Una aplicación en **Flet** consume la API para visualizar los datos en tiempo real.

---

## 🚀 Configuración en AWS
### 1️⃣ **Crear la Tabla en DynamoDB**
- Nombre de la tabla: `esp32_data`
- **Clave primaria:** `device_id (String)`
- **Atributos:**
  - `device_id (String)` → ID del dispositivo.
  - `temperatura (Number)` → Temperatura del sensor.
  - `humedad (Number)` → Humedad medida.
  - `led (Boolean)` → Estado del LED.
  - `timestamp (Number)` → Marca de tiempo en milisegundos.

### 2️⃣ **Configurar Lambda Function**
Usamos **una sola Lambda** para manejar tanto **GET** (lectura) como **POST** (escritura).

#### Código de la Lambda:
```python
import json
import boto3
import decimal
import time
import os

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ.get("DYNAMODB_TABLE", "esp32_data")
table = dynamodb.Table(TABLE_NAME)

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    try:
        print("Evento recibido:", event)
        http_method = event.get("httpMethod", "")
        
        if http_method == "GET":
            params = event.get("queryStringParameters", {})
            device_id = params.get("device_id") if params else None
            if not device_id:
                return {"statusCode": 400, "body": json.dumps({"error": "device_id es requerido"})}
            
            response = table.get_item(Key={"device_id": device_id})
            if "Item" not in response:
                return {"statusCode": 404, "body": json.dumps({"error": "Dispositivo no encontrado"})}
            
            return {"statusCode": 200, "body": json.dumps(response["Item"], cls=DecimalEncoder)}

        elif http_method == "POST":
            data = json.loads(event["body"]) if "body" in event else event  
            
            device_id = data.get("device_id")
            temperatura = decimal.Decimal(str(data.get("temperatura", 0)))
            humedad = decimal.Decimal(str(data.get("humedad", 0)))
            led = data.get("led", False)
            timestamp = int(time.time() * 1000)  

            if not device_id:
                return {"statusCode": 400, "body": json.dumps({"error": "device_id es requerido"})}
            
            item = {
                "device_id": device_id,
                "temperatura": temperatura,
                "humedad": humedad,
                "led": led,
                "timestamp": timestamp
            }
            table.put_item(Item=item)

            return {"statusCode": 200, "body": json.dumps({"message": "Datos guardados correctamente"}, cls=DecimalEncoder)}

        return {"statusCode": 405, "body": json.dumps({"error": "Método no permitido"})}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
```

### 3️⃣ **Configurar API Gateway**
- Crear una API REST en **API Gateway**.
- Crear dos métodos **GET** y **POST** enlazados con la Lambda.
- Habilitar **CORS** en ambos métodos.
- Añadir una API Key y activarla en los métodos.

---

## 📡 **ESP32: Código para enviar datos**
El ESP32 está configurado para **publicar datos a AWS IoT Core** usando MQTT. Luego, IoT Core redirige los datos a la Lambda para almacenarlos en DynamoDB.

```cpp
void publicarDatos() {
    JsonDocument doc;
    doc["device_id"] = "esp32-01";
    doc["temperatura"] = 25.4;
    doc["humedad"] = 60;
    doc["led"] = ledState;
    doc["timestamp"] = millis();
    
    char buffer[256];
    serializeJson(doc, buffer);
    client.publish("esp32/data", buffer);
}
```

---

## 🛠️ **Pruebas con cURL**

### **✅ Enviar datos con POST**
```sh
curl -X POST -H "Content-Type: application/json" \
-H "x-api-key: TtoFJcetia6H8PIk83fXT4HiAowaqJiG2UJSXYFe" \
-d '{"device_id": "esp32-01", "temperatura": 26.5, "humedad": 55, "led": true}' \
"https://a0krgo2aca.execute-api.us-west-1.amazonaws.com/dev_env/esp32"
```

### **✅ Leer datos con GET**
```sh
curl -H "x-api-key: TtoFJcetia6H8PIk83fXT4HiAowaqJiG2UJSXYFe" \
"https://a0krgo2aca.execute-api.us-west-1.amazonaws.com/dev_env/esp32?device_id=esp32-01"
```

---

## 📊 **Siguiente paso: Integración con Flet**
Ahora que la API funciona correctamente, el siguiente paso es conectar nuestra aplicación en **Flet** para visualizar los datos. 🚀

1. **Modificar el código de Flet** para hacer peticiones GET y POST a la API.
2. **Mostrar los datos en gráficos interactivos**.
3. **Configurar widgets para monitoreo en tiempo real**.

# 📘 Documentación: ESP32 IoT Dashboard con Flet

## 📌 **Descripción del Proyecto**
Esta aplicación de escritorio, desarrollada con **Flet**, permite visualizar y gestionar dispositivos ESP32 conectados a AWS IoT.

El sistema permite:
- 📡 **Recibir datos en tiempo real** desde DynamoDB mediante una API Gateway.
- 📊 **Visualizar datos en gráficos personalizables**.
- 🔧 **Configurar dispositivos y widgets** desde una interfaz gráfica.
- 🔄 **Actualizar la configuración y conectar con AWS IoT**.

---

## 📌 **Estructura del Proyecto**
📂 **ESP32_Dashboard/** _(Directorio principal)_
- 📄 `main.py` _(Código principal de la aplicación Flet)_
- 📄 `config.json` _(Configuración guardada de la API y claves)_
- 📂 `data/` _(Almacena archivos locales de dispositivos)_
- 📂 `assets/` _(Recursos gráficos si son necesarios)_

---

## 📌 **Configuración de la Aplicación**

La aplicación guarda su configuración en un **archivo JSON** ubicado en una carpeta estándar del sistema operativo:

| Sistema Operativo | Ubicación de `config.json` |
|------------------|-------------------------|
| 🖥️ Windows | `C:\Users\usuario\AppData\Local\ESP32_Dashboard\config.json` |
| 🐧 Linux/macOS | `~/.config/ESP32_Dashboard/config.json` |

El archivo **`config.json`** contiene:
```json
{
    "API_URL": "https://a0krgo2aca.execute-api.us-west-1.amazonaws.com/dev_env/esp32",
    "API_KEY": "TtoFJcetia6H8PIk83fXT4HiAowaqJiG2UJSXYFe",
    "DATA_FILE": "C:/Users/usuario/AppData/Local/ESP32_Dashboard/devices_data.json"
}
```

**📌 Configuración Automática**
Si `config.json` no existe, la aplicación lo creará automáticamente.

---

## 📌 **Instalación y Ejecución**

### 1️⃣ **Requisitos Previos**
- ✅ Python 3.11+
- ✅ Instalar dependencias:
  ```sh
  pip install flet requests
  ```

### 2️⃣ **Ejecución de la Aplicación**
```sh
python main.py
```
---

## 📌 **Interfaz de Usuario (UI)**

La aplicación tiene 3 pestañas principales:

🔹 **Administrar ESP32** → Agregar dispositivos, configurar widgets.  
🔹 **Visualizar Datos** → Mostrar gráficos con los datos en tiempo real.  
🔹 **Configuración** → Modificar la URL de la API y claves de acceso.

---

## 📌 **Funcionamiento del Código**

### 🔹 **Carga y Guarda de Configuración**
El sistema gestiona la configuración de manera automática:
```python
import os, json

CONFIG_DIR = os.path.join(os.getenv("APPDATA"), "ESP32_Dashboard")
os.makedirs(CONFIG_DIR, exist_ok=True)
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
```

### 🔹 **Conexión con la API Gateway**
Los datos se obtienen mediante una petición HTTP GET:
```python
headers = {"x-api-key": API_KEY}
response = requests.get(f"{API_URL}?device_id={self.device_id}", headers=headers)
```

### 🔹 **Gestión de Dispositivos**
Cada ESP32 se maneja como una clase `Esp32Device`:
```python
class Esp32Device(ft.Column):
    def __init__(self, device_id, remove_device_callback, widgets=None):
        super().__init__()
        self.device_id = device_id
        self.widgets = widgets if widgets else []
```

### 🔹 **Interfaz con Flet**
Los elementos se agregan dinámicamente a la UI:
```python
pestañas = [
    ft.Tab(text="Administrar ESP32", content=ft.Column([])),
    ft.Tab(text="Visualizar Datos", content=ft.Column([])),
    ft.Tab(text="Configuración", content=ft.Column([]))
]
```

---

## 📌 **Mejoras Futuras**
🔹 Soporte para más tipos de sensores.  
🔹 Guardado local de datos para análisis offline.  
🔹 Autenticación para acceso seguro.  

🚀 **¡Listo para monitorear tus ESP32 con una app moderna y escalable!** 🎉

