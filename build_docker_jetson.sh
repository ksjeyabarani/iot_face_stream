echo "Build Facedetector\n"
docker build -t facedetector -f Dockerfile.facedetector .

echo "Build Forwarder\n"
docker build -t forwarder -f Dockerfile.forwarder .

echo "Build Mosquitto Broker\n"
docker build -t mosquitto -f Dockerfile.mosquitto .

