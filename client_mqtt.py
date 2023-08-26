import time
import paho.mqtt.client as mqtt_client
import paho.mqtt.subscribe as subscribe
import paho.mqtt.publish as publish
from paho import mqtt
import ssl
import paho.mqtt.properties as properties
import database

class MqttClient:
    _CLIENT = mqtt_client.Client()
    _SERVER : str = "6cadf8dab28a4327b9ea16c3944ce5b4.s2.eu.hivemq.cloud"
    _PORT : int = 8883
    _USER : str  = "pruebajara"
    _PASSWORD : str  = "123498765"

    def __init__(self) -> None:
        pass

    def __init__(self) -> None:
        MqttClient.client = mqtt_client.Client(client_id = "", userdata = None, protocol = mqtt_client.MQTTv5)
        MqttClient.client.tls_set(tls_version = mqtt.client.ssl.PROTOCOL_TLS)
        MqttClient.client.username_pw_set(MqttClient._USER, MqttClient._PASSWORD)
        connect_properties = properties.Properties(properties.PacketTypes.CONNECT)
        connect_properties.SessionExpiryInterval = 3600
        MqttClient.client.connect(MqttClient._SERVER, MqttClient._PORT, keepalive=60, clean_start = False, properties=connect_properties)
        MqttClient.client.on_connect = on_connect
        MqttClient.client.on_subscribe = on_subscribe
        MqttClient.client.on_message = on_message
        MqttClient.client.on_publish = on_publish
    
    def __del__(self):
        MqttClient.client.disconnect()

    def subscribe(self, message : str, quality: int) -> bool:
        MqttClient.client.subscribe(message, qos = quality)

    def get_messages(self) -> None:
        print("Inside on get_messages")
        MqttClient.client.loop_forever()
    
    def publish(self, topic : str, message :  str, quality = int) -> None:
        MqttClient.client.publish(topic, payload = message, qos=quality, retain = False)
        print("enviando mensaje")

    def delete_retained(self, topic : str, message :  str, quality = int) -> None:
        MqttClient.client.publish(topic, "", 0, True)

    def get_all_messages(self) -> None:
        auth = {'username': f"{MqttClient._USER}", 'password': f"{MqttClient._PASSWORD}"}
        sslSettings = ssl.SSLContext(mqtt.client.ssl.PROTOCOL_TLS)
        subscribe.callback(get_msg, "#", hostname = MqttClient._SERVER, port = MqttClient._PORT, auth = auth, tls = sslSettings, protocol = mqtt_client.MQTTv311)

    def disconect() -> None:
        MqttClient.client.disconnect()


def on_connect(client, userdata, flags, rc, properties = None) -> None:
    print("CONNACK received with code %s." % rc)

def on_publish(client, userdata, mid, properties = None) -> None:
    print("mid: " + str(mid))

def on_subscribe(client, userdata, mid, granted_qos, properties = None) -> None:
    print("inside on_Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg) -> str:
    print("Inside on on_message")
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    database.execute_insert(f"insert into general.messages(message, flag, timestamp, state, qos, topic) values('{msg.payload}', 'False', '{msg.timestamp}', '{msg.state}', '{msg.qos}', '{msg.topic}')")
    database.write_file(msg.topic, msg.payload, msg.qos, msg.timestamp)
    
    
    
def get_msg(client, userdata, message) -> str:
    try:
        line = message.topic + " " + str(message.payload) + "\n"
        print(line)
        return line
    except Exception as ex:
        print("Se ha generado ub error", ex)
        return ""





"""with open("demo.txt") as file:
print(file.readline(7))
with open("lista_compras.txt") as archivo:
print(archivo.readlines())
archivo.read()
archivo.close()
"""






"""
msgs = [{'topic': "paho/test/multiple", 'payload': "test 1"}, ("paho/test/multiple", "test 2", 0, False)]

# use TLS for secure connection with HiveMQ Cloud
sslSettings = ssl.SSLContext(mqtt.client.ssl.PROTOCOL_TLS)

# put in your cluster credentials and hostname
auth = {'username': "<username>", 'password': "<password>"}
publish.multiple(msgs, hostname="<hostname>", port=8883, auth=auth, tls=sslSettings, protocol=paho.MQTTv31)
"""
