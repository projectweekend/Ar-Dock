import time
import RPi.GPIO as gpio
from serial import Serial
from settings import sensors_config as config
from lighting import Bridge
from utils.parse import parse_sensor_data


# setup serial port
if config['serial_connection'] == 'gpio':
    print("Serial connection: GPIO")
    SERIAL = Serial('/dev/ttyAMA0', config['serial_rate'])
else:
    print("Serial connection: USB")
    SERIAL = Serial('/dev/ttyUSB0', config['serial_rate'])

# wait 2 seconds for serial port to finish initializing
time.sleep(2)


# setup motion detector stuff
DETECTION_TIMEOUT = 180
MOTION_PIN = 18
LUMINOSITY_THRESHOLD = 2.0

gpio.setmode(gpio.BCM)
gpio.setup(MOTION_PIN, gpio.IN, initial=gpio.LOW, pull_up_down=gpio.PUD_DOWN)


def main():

    hue = Bridge()

    while True:

        gpio.wait_for_edge(MOTION_PIN, gpio.RISING)

        # send 'L' to let Ar-Starbug know we want a luminosity reading
        SERIAL.write('L')

        # convert raw serial string to dictionary
        sensor_data = parse_sensor_data(SERIAL.readline())

        if sensor_data['luminosity'] <= LUMINOSITY_THRESHOLD:
            hue.lights_on()
            time.sleep(DETECTION_TIMEOUT)


if __name__ == '__main__':
    main()
