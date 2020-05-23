import common
import paho.mqtt.client as mqtt
import time
import traceback

timestamp=str(int(time.time()))
counter = 0
ROOT_DIR="/mnt/mybucket"

def on_connect_local(client, userdata, flags, rc):
    print("Image Saver connected to local broker with rc: " + str(rc))
    client.subscribe(common.LOCAL_MQTT_TOPIC)

def get_next_file():
    global counter
    name = "{0}/image_{1}_{2}.png".format(ROOT_DIR, timestamp, str(counter).zfill(6));
    counter += 1
    return name

def on_message(client,userdata, msg):
    try:
        file_path=get_next_file()
        print("Got Message of length : {0}, Going to write to {1}".format(len(msg.payload), file_path))
        with open(file_path, "wb") as f:
            f.write(msg.payload)
    except:
        traceback.print_exc()
        print("Unexpected error:", sys.exc_info()[0])
        raise


local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(common.LOCAL_MQTT_HOST, common.LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()

