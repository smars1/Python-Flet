import os
from dotenv import load_dotenv

# Cargar las variables desde el archivo .env
load_dotenv()

# Variables de AWS IoT Core y DynamoDB
AWS_IOT_ENDPOINT = os.getenv("AWS_IOT_ENDPOINT")
DYNAMODB_TABLE = os.getenv("DYNAMODB_TABLE")

# Credenciales MQTT
MQTT_USERNAME = os.getenv("MQTT_USERNAME")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")

# Depuración (puedes desactivar esto en producción)
print(f"AWS IoT Endpoint: {AWS_IOT_ENDPOINT}")
print(f"DynamoDB Table: {DYNAMODB_TABLE}")
