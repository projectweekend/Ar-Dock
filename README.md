## Background

This is a Raspberry Pi project that works directly with one of my Arduino projects: [Ar-Starbug](https://github.com/projectweekend/Ar-Starbug). These two projects combine to replace two older ones: [Pi-Starbug](https://github.com/projectweekend/Pi-Starbug) and [Pi-Nova-5](https://github.com/projectweekend/Pi-Nova-5). The sensor logic for each older project has been moved off of a Raspberry Pi and onto an Arduino. This new structure:

* Let's the Arduino do what it does best: run a small, fast loop and read data from various sensors. It can communicate with the Raspberry Pi using both digital GPIO pins and serial when needed.
* Frees up one of my Raspberry Pis. Instead of using two, now I only need one. Also since this project is designed to report the data it collects back to another [project](https://github.com/projectweekend/Holly), the Pi is a perfect fit. Connecting an Arduino to the internet and sending/receiving data is misreably tedious in my opinion. The Pi does a much better job.

## Project Info

* `environmental_sensors.py`: This Python script is called by a Cron job. It reads data over the serial port (USB or GPIO), then makes a POST request to the an HTTP end point sending the data it collected. The messaging interface used over the serial port is designed to communicate with my [Ar-Starbug](https://github.com/projectweekend/Ar-Starbug) project, but that could be altered to work with something else.

* `motion_detector.py`: This Python script is used by an Upstart job. It waits to detect an edge on a GPIO pin where a PIR motion sensor is meant to be connected. When it receives the edge, it checks the luminosity reading from a sensor on my [Ar-Starbug](https://github.com/projectweekend/Ar-Starbug) project via the serial port. If the reading is below the threshold it makes a POST to the Philips HUE API and turns on the lights.

## Config

Custom configurations are stored in an untracked file at the root of the project: `config.yml`. The following is an example of what that file should look like:
```
sensors:
    serial_connection: gpio
    serial_rate: 9600
    data_frequency: 15
    sensor_data_url: https://your.json-endpoint.com/api/sensor
    system_data_url: https://your.json-endpoint.com/api/raspberry-pi
bean:
    mac_address: mac_address_for_bean
    characteristic_uuid: characteristic_bank_uuid_value
```


## BlueZ

This project requires the BlueZ Bluetooth stack and the BluePy Python library. The easiest way to install both of those is to use the Raspberry Pi setup script I made: [http://projectweekend.github.io/Pi-Setup/](http://projectweekend.github.io/Pi-Setup/)

