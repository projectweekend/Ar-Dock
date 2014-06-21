import os
import time
import serial
import thread


SEND_FREQ = os.getenv('AR_DOCK_TRANSMIT_FREQ', 15)
CONNECTION_TYPE = os.getenv('AR_DOCK_CONNECTION_TYPE', 'usb')
DATA_RATE = os.getenv('AR_DOCK_DATA_RATE', 9600)

if CONNECTION_TYPE == 'gpio':
    # setup GPIO serial
    pass
else:
    SERIAL = serial.Serial('/dev/ttyUSB0', DATA_RATE)
time.sleep(2)


def main():
    while True:
        data = SERIAL.readline()
        print(data)
        time.sleep(SEND_FREQ * 60)


if __name__ == '__main__':
    main()
