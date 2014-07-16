#!/usr/bin/env python

import time
from serial import Serial
from threading import Thread
from settings import sensors_config as config
from utils.http import json_post
from utils.parse import parse_sensor_data
from utils.log import log_config_error


if config['serial_connection'] == 'gpio':
    print("Serial connection: GPIO")
    SERIAL = Serial('/dev/ttyAMA0', config['serial_rate'])
else:
    print("Serial connection: USB")
    SERIAL = Serial('/dev/ttyUSB0', config['serial_rate'])

# wait 2 seconds for serial port to finish initializing
time.sleep(2)


def main():

    # send 'A' to let Ar-Starbug know we want all sensor readings
    SERIAL.write('A')

    # convert raw serial string to dictionary
    sensor_data = parse_sensor_data(SERIAL.readline())

    # post data to server in another thread
    try:
        Thread(target=json_post, args=(config['sensor_data_url'], sensor_data)).start()
    except KeyError:
        log_config_error("'sensor_data_url' is not defined in 'config.yml'")


if __name__ == '__main__':
    main()
