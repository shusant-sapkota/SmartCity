import os
from confluent_kafka import SerializingProducer
from datetime import datetime
import simplejson as json

LONDON_COORDINATES = {"latitude": 51.5074,"logitude": -0.1278}
BIRMINGHAM_COORDINATES = {"latitude": 52.4862,"logitude": -1.8904}

# Calculate the movement increment.
LATITUDE_INCREMENT = (BIRMINGHAM_COORDINATES['latitude']-LONDON_COORDINATES['latitude'])/100
LONGITUDE_INCREMENT = (BIRMINGHAM_COORDINATES['longitude']-LONDON_COORDINATES['longitude'])/100

#Environment Variable for Configuratio
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
VEHICLE_TOPIC = os.getenv('VEHICLE_TOPIC', 'vehicle_data')
GPS_TOPIC = os.getenv('GPS_TOPIC', 'gps_data')
TRAFFIC_TOPIC = os.getenv('TRAFFIC_TOPIC', 'traffic_data')
WEATHER_TOPIC = os.getenv('WEATHER_TOPIC', 'weather_data')
EMERGENCY_TOPIC = os.getenv('EMERGENCY_TOPIC', 'emergency_data')

start_time = datetime.now()
start_location = LONDON_COORDINATES.copy()

if __name__ == "__main__"():
    producer_config = {
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS.
    }


