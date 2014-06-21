import time
import serial
from settings import CONNECTION_TYPE, DATA_RATE


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
        time.sleep(1)


if __name__ == '__main__':
    main()
