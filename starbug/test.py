import time
import serial
import click


@click.command()
@click.option('--type', default='usb', help='The serial connection type: usb or gpio')
@click.option('--rate', default=9600, help='The serial data rate (defaults to 9600)')
def main(type, rate):
    if type == 'pin':
        # make this work
        pass
    else:
        SERIAL = serial.Serial('/dev/ttyUSB0', data_rate)
    # Give serial port a little time to setup
    time.sleep(2)
    while True:
        data = SERIAL.readline()
        print(data)
        time.sleep(1)


if __name__ == '__main__':
    main()
