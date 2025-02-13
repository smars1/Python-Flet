import paho.mqtt.client as mqtt
from config import AWS_IOT_ENDPOINT, MQTT_USERNAME, MQTT_PASSWORD

class MQTTManager:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.connect()

    def on_connect(self, client, userdata, flags, rc):
        """Callback cuando el cliente se conecta a MQTT"""
        print(f"Conectado a AWS IoT Core con código {rc}")
        client.subscribe("iot/#")  # Suscribirse a todos los tópicos

    def on_message(self, client, userdata, message):
        """Callback cuando se recibe un mensaje MQTT"""
        print(f"Mensaje recibido en {message.topic}: {message.payload.decode()}")

    def publish(self, topic, message):
        """Publicar un mensaje en MQTT"""
        self.client.publish(topic, message)
        print(f"Publicado en {topic}: {message}")

    def connect(self):
        """Conectar al broker MQTT"""
        self.client.connect(AWS_IOT_ENDPOINT, 8883)
        self.client.loop_start()

# Instancia global de MQTTManager
mqtt_manager = MQTTManager()
