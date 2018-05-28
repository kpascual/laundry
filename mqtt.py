import paho.mqtt.client as mqtt
import sms


THRESHOLD = 0.0001


def on_connect(client, userdata, flags, rc):
    client.subscribe("laundry")   


def on_message(client, userdata, msg):
    userdata['val'] = (userdata['val'] * userdata['weight_past']) + (int(msg.payload) * userdata['weight_present'])


    if userdata['val'] < THRESHOLD and userdata['is_notified'] == 0:
        sms.textMe("Your laundry is complete. Go get it now.")
        userdata['is_notified'] = 1
        print("User notified")

    print (msg.payload, userdata['val'])


client_params = {
    'val': 1,
    'weight_past': 0.998,
    'weight_present': 0.1,
    'is_notified': 0
}

client = mqtt.Client(userdata=client_params)
client.on_connect = on_connect
client.on_message = on_message


client.connect("localhost", 1883, 60)

client.loop_forever()
