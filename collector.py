from client_mqtt import MqttClient


cli = MqttClient()
#cli.get_all_messages()
cli.subscribe("#", 0)
cli.get_messages()
