import os
import random
import time
import uuid




MANHATTAN_COORDINATES = {"latitude": 40.7831, "longitude": -73.9712}
BINGHAMTON_COORDINATES = {"latitude": 42.0987, "longitude": -75.9180}

# Calculate movement increments
LATITUDE_INCREMENT = (BINGHAMTON_COORDINATES['latitude'] - MANHATTAN_COORDINATES['latitude']) / 100
LONGITUDE_INCREMENT = (BINGHAMTON_COORDINATES['longitude'] - MANHATTAN_COORDINATES['longitude']) / 100

# Environment Variables for configuration
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
VEHICLE_TOPIC = os.getenv('VEHICLE_TOPIC', 'vehicle_data')
GPS_TOPIC = os.getenv('GPS_TOPIC', 'gps_data')
TRAFFIC_TOPIC = os.getenv('TRAFFIC_TOPIC', 'traffic_data')
WEATHER_TOPIC = os.getenv('WEATHER_TOPIC', 'weather_data')
EMERGENCY_TOPIC = os.getenv('EMERGENCY_TOPIC', 'emergency_data')



if __name__ == "__main__":
    producer_config = {
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
        'error_cb': lambda err: print(f'Kafka error: {err}')
    }
    producer = SerializingProducer(producer_config)

    try:
        simulate_journey(producer, 'Vehicle-Onkar')

    except KeyboardInterrupt:
        print('Simulation ended by the user')
    except Exception as e:
        print(f'Unexpected Error occurred: {e}')