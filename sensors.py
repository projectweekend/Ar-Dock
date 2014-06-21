import time
from serial import Serial
from threading import Thread
from settings import sensors_config as config
from utils.http import json_post
from utils.parse import parse_sensor_data


if config['serial_connection'] == 'gpio':
    SERIAL = Serial('/dev/ttyAMA0', config['serial_rate'])
else:
    SERIAL = Serial('/dev/ttyUSB0', config['serial_rate'])

# wait 2 seconds for serial port to finish initializing
time.sleep(2)


def main():
    while True:
        # convert raw serial string to dictionary
        sensor_data = parse_sensor_data(SERIAL.readline())
        # post data to server in another thread
        Thread(target=json_post, args=(config['data_url'], sensor_data)).start()
        # hang out until time to do it again
        time.sleep(config['data_frequency'] * 60)


if __name__ == '__main__':
    main()
