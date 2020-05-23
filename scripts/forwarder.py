import common
import paho.mqtt.client as mqtt


def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(common.LOCAL_MQTT_TOPIC)

def on_connect_remote(client, userdata, flags, rc):
    print("connected to remote broker with rc: " + str(rc))

remote_mqttclient = mqtt.Client()
remote_mqttclient.on_connect = on_connect_remote
print("Forwarder connecting to remote mqtt host : {0}".format(common.REMOTE_MQTT_HOST))

remote_mqttclient.connect(common.REMOTE_MQTT_HOST, common.REMOTE_MQTT_PORT, 60)

def on_message(client,userdata, msg):
    try:
        print("Forwarding Message Length : {}".format(len(msg.payload)))
        remote_mqttclient.publish(common.REMOTE_MQTT_TOPIC, payload=msg.payload, qos=0, retain=False)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(common.LOCAL_MQTT_HOST, common.LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()

    
