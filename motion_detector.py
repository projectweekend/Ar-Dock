import time
from serial import Serial
from btle import Peripheral
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

LUMINOSITY_THRESHOLD = 2.0
READ_INTERVAL = 3
DETECTION_TIMEOUT = 7200


def main():

    hue = Bridge()

    while True:

        detector_value = read_motion_detector()

        if detector_value == 1:

            # send 'L' to let Ar-Starbug know we want a luminosity reading
            SERIAL.write('L')

            # convert raw serial string to dictionary
            sensor_data = parse_sensor_data(SERIAL.readline())

            if sensor_data['luminosity'] <= LUMINOSITY_THRESHOLD:
                hue.lights_on()
                time.sleep(DETECTION_TIMEOUT)

            time.sleep(READ_INTERVAL)


def read_motion_detector():
    p = Peripheral("D0:39:72:C8:C9:6B")
    characteristics = p.getCharacteristics(uuid="A495FF21-C5B1-4B44-B512-1370F02D74DE")
    if len(characteristics) != 1:
        # no data from Bean...send some kind of message
        return None
    value = characteristics[0].read()
    p.disconnect()
    return value


if __name__ == '__main__':
    main()
