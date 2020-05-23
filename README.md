## Notes

I have used docker compose to orchestrate different containers in jetson and cloud hosts. 

## Topic Name:

I have used the topic name as "face_stream" in both MQTT brokers. As the topic only is a realtime stream of cropped out face-images coming from USB camera, I thought face_stream would be appropriate naming.

I have kept the QOS to be 0 (atmost 1) which is best effort and involves low overhead given that we are using an edge IOT device. Also, since it a realtime feed, it is ok to have message losses. Hence, I chose that QOS level. 


## Setup

### Environment

Change environmnet file to provide correct cloud host and bucket name. The S3 Bucket URL is currently hardcoded in scripts/image_saver.py. Please change it if you are using a different region.

### Step 1: In Cloud Host 

1. Run ./setup_docker_cloud.sh
     This will install docker and docker-compose in cloud Host

2. Run ./build_docker_cloud.sh
      This will build 2 docker images as mentioned in the architecture

3. Run docker-compose -f docker-compose-cloud-hw03.yml up
      This will run docker-compose which will start mosquitto broker and image saver docker containers.

### Step 2: In Jetson Host

1. Run ./setup_docker_jetson.sh
     This will install docker-compose in Jetson Host

2. Run ./build_docker_jetson.sh
      This will build 3 docker images as mentioned in the architecture

3. Run docker-compose -f docker-compose-jetson-hw03.yml up
      This will run docker-compose which will start mosquitto broker, facedetect and image forwarder docker containers. Facedetect will start sending face images every 1 second. At this point, you should be able to see images getting added to S3 bucket.


## Location

Please find the images under the URL : https://s3.us-east.objectstorage.softlayer.net/cloud-object-storage-h2-cos-standard-bsp/
(E.g: https://s3.us-east.objectstorage.softlayer.net/cloud-object-storage-h2-cos-standard-bsp/image_1590228604_000006.png)


