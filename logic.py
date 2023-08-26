from client_mqtt import *
import threading
from time import sleep

class DatabaseAdmin:

    def __init__(self) -> None:
        self.client = MqttClient()
        self.thread = threading.Thread()
      
    def send_data(self, topic : str, messages : list) -> None:
        for _ in messages:
            self.client.publish(topic, _ , 2)

    def send_message(self, topic : str, message : str) -> None:
        self.client.publish(topic, message , 2)

    def get_data(self) -> None:
        self.client.subscribe("#", 0)
        self.thread = threading.Thread(target = self.client.get_messages, name = 'get_messages')
        self.thread.start()

    def estado(self) -> bool:
        print("Esta activo?: ", str(self.thread.is_alive()))
        return self.thread.is_alive()
    
    def stop_retrieve(self):
        self.thread.join()

    def retrieve_messages(self) -> None:
        return database.execute_select("SELECT * from general.topics")
        

class NullException(Exception):
    pass





