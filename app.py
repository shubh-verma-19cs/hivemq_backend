from flask import Flask
from flask_mqtt import Mqtt
import flask_mqtt

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = '0.0.0.0'
app.config['MQTT_BROKER_PORT'] = 1883
# app.config['MQTT_USERNAME'] = 'user1'
# app.config['MQTT_PASSWORD'] = 'pass1'
app.config['MQTT_REFRESH_TIME'] = 60.0

mqtt = Mqtt(app)

# Debug setting set to true
app.debug = True


@app.route('/')
def index():
    return "Hello World on Flask"

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('home/mytopic')
    mqtt.publish('home/mytopic','hello world',1,True)

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )

@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    if level == flask_mqtt.MQTT_LOG_ERR:
        print('Error: {}'.format(buf))

if __name__ == '__main__':
    app.run()
