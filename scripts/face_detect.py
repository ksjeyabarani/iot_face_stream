import cv2
import common
import paho.mqtt.client as mqtt
import time

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv2.VideoCapture(1)

face_cascade = cv2.CascadeClassifier('/usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

local_mqttclient = mqtt.Client()
local_mqttclient.connect(common.LOCAL_MQTT_HOST, common.LOCAL_MQTT_PORT, 60)

counter = 0

try:
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # We don't use the color information, so might as well save space
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # gray here is the gray frame you will be getting from a camera
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            # your logic goes here; for instance
            # cut out face from the frame..
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            face = frame[y:y+h, x:x+w]
            rc, png = cv2.imencode('.png', face)
            msg = png.tobytes()
            print("Sending Message Length : {}".format(len(msg)))
            local_mqttclient.publish(common.LOCAL_MQTT_TOPIC, payload=msg, qos=0, retain=False)
        # Sleep for 1 sec
        time.sleep(1)
except:
    print("Got error")

cap.release()
cv2.destroyAllWindows()
