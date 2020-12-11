import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

led = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)


#function after connecting to server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("test")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    message = msg.payload.decode(encoding='UTF-8',errors='strict')
    #print("Bulb is turned", message) #printing payload in correct format

    if message == 'on':
        GPIO.output(led, GPIO.HIGH)

    elif message == 'off':
        GPIO.output(led, GPIO.LOW)



    #print(msg.topic+" "+str(msg.payload))

client = mqtt.Client("Ashay-PC") #assigning client ID
client.username_pw_set(username="sventech",password="sventech") #assigning server credentials
client.on_connect = on_connect
client.on_message = on_message

client.connect("3.135.196.249", 1883, 60) #connecting to server

client.loop_forever()