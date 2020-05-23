import os

LOCAL_MQTT_HOST="mosquitto"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="face_stream"

REMOTE_MQTT_HOST=os.getenv("CLOUD_HOST", "169.45.115.148")
REMOTE_MQTT_PORT=1883
REMOTE_MQTT_TOPIC="face_stream"

S3_BUCKET=os.getenv("S3_BUCKET_NAME", "cloud-object-storage-h2-cos-standard-bsp")
