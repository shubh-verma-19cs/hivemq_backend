import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("$SYS/#")
    client.subscribe("mytopic", 1)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


def on_subscribe(client, userdata, mid, granted_qos):
    publish.single("mytopic", "Hello World", 1, retain=True, hostname="0.0.0.0", auth = {'username':"admin-user", 'password':"admin-password"})


client = mqtt.Client()

client.username_pw_set(username="admin-user", password="admin-password")

client.connect("0.0.0.0", 1883, keepalive=5)
client.on_connect = on_connect
# client.on_subscribe = on_subscribe
client.on_message = on_message

# publish.single("mytopic", "Hello World", 1, retain=True, hostname="0.0.0.0", auth = {'username':"user1", 'password':"pass1"})
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
