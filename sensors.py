import os
import time
from serial import Serial
from threading import Thread
from utils.http import json_post
from utils.parse import parse_sensor_data


SEND_FREQ = os.getenv('AR_DOCK_SENSOR_SEND_FREQ', 15)
SEND_URL = os.getenv('AR_DOCK_SENSOR_SEND_URL', 'http://holly.local/api/starbug/data')
CONNECTION_TYPE = os.getenv('AR_DOCK_SERIAL_CONNECTION_TYPE', 'usb')
DATA_RATE = os.getenv('AR_DOCK_SERIAL_DATA_RATE', 9600)

if CONNECTION_TYPE == 'gpio':
    SERIAL = Serial('/dev/ttyAMA0', DATA_RATE)
else:
    SERIAL = Serial('/dev/ttyUSB0', DATA_RATE)

# wait 2 seconds for serial port to finish initializing
time.sleep(2)


def main():
    while True:
        # convert raw serial string to dictionary
        sensor_data = parse_sensor_data(SERIAL.readline())
        # post data to server in another thread
        Thread(target=json_post, args=(SEND_URL, sensor_data)).start()
        # hang out until time to do it again
        time.sleep(SEND_FREQ * 60)


if __name__ == '__main__':
    main()
