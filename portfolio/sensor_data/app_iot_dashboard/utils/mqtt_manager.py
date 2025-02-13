import paho.mqtt.client as mqtt

class MQTTManager:
    def __init__(self, broker, port, topic_subscribe="iot/#"):
        self.broker = broker
        self.port = port
        self.topic_subscribe = topic_subscribe
        self.client = mqtt.Client()

        # Asignar los callbacks
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        # Conectar al broker MQTT
        self.connect()

    def on_connect(self, client, userdata, flags, rc):
        """Callback cuando el cliente se conecta a MQTT"""
        print(f"Conectado a MQTT Broker: {self.broker}, Código: {rc}")
        client.subscribe(self.topic_subscribe)  # Suscribirse al tópico

    def on_message(self, client, userdata, message):
        """Callback cuando se recibe un mensaje MQTT"""
        print(f"Mensaje recibido en {message.topic}: {message.payload.decode()}")

    def publish(self, topic, message):
        """Publicar un mensaje en un tópico MQTT"""
        self.client.publish(topic, message)
        print(f"Publicado en {topic}: {message}")

    def connect(self):
        """Iniciar la conexión al broker MQTT"""
        self.client.connect(self.broker, self.port)
        self.client.loop_start()  # Iniciar el loop en segundo plano

    def disconnect(self):
        """Desconectar del broker MQTT"""
        self.client.loop_stop()
        self.client.disconnect()
        print("Desconectado del MQTT Broker")

# Crear instancia de MQTTManager con los datos de AWS IoT Core
mqtt_manager = MQTTManager(
    broker="a3kh5bh54fkq13-ats.iot.us-west-1.amazonaws.com",
    port=8883,
    topic_subscribe="esp32/update"
)
