echo "Build Mosquitto Broker\n"
docker build -t mosquitto -f Dockerfile.mosquitto .

echo "Build Image Saver\n"
docker build -t saver -f Dockerfile.saver .
