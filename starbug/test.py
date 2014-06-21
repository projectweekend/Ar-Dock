import time
import serial


SERIAL = serial.Serial('/dev/tty.usbserial-A5027VO5', 9600)
time.sleep(5)


def main():
    while True:
        data = SERIAL.readline()
        print(data)
        time.sleep(1)


if __name__ == '__main__':
    main()
