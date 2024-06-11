import paho.mqtt.client as mqtt
from django.conf import settings
from devices.models import CollectedData, Stac

def on_connect(mqtt_client, userdata, flags, rc):
   if rc == 0:
       print('Connected successfully')
       mqtt_client.subscribe('flux/mqtt')
   else:
       print('Bad connection. Code:', rc)
       
def on_message(mqtt_client, userdata, msg):
    stac = Stac.objects.get(id=1)
    CollectedData.objects.create(data=msg.payload.decode('utf-8'), stac=stac)
    print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')
   
   
   
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)