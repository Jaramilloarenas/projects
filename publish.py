from client_mqtt import MqttClient

cli = MqttClient()
counter = 0

try:
    while(input("Otro topico y/n: ") == "y"):

        cli.publish("verificacion", "Mensaje 111 " + str(counter), 2)
        cli.publish("another", "Mensaje 1" + str(counter), 2)
        cli.publish("another", "Mensaje 22 " + str(counter), 2)
        cli.publish("another", "Mensaje 33 " + str(counter), 2)
        cli.publish("another", "Mensaje 44 " + str(counter), 2)
        cli.publish("prueba", "Mensaje " + str(counter), 2)
        

        """cli.publish("verificacion", "", 0)
        #cli.publish("#", " ", 2)
        cli.publish("lacaravana", "", 0)
        cli.publish("another", "", 0)
        cli.publish("another", "", 0)
        cli.publish("another", "", 0)
        cli.publish("another", "", 0)
        cli.publish("prueba", "", 0)
        cli.publish("verificaction", "", 0)""" 
        counter += 1
        print("counter: ", counter)

except Exception as ex:
    print("Se ha generado un error intentando conectar", ex)
