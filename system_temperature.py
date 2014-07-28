#!/usr/bin/env python

import subprocess
from threading import Thread
from settings import sensors_config as config
from utils.http import json_post
from utils.log import log_config_error


SHELL_COMMAND = ["/opt/vc/bin/vcgencmd", "measure_temp"]


def celsius_to_fahrenheit(celsius_value):
    return (celsius_value * (9.0/5.0)) + 32


def get_system_temp():
    system_result = subprocess.check_output(SHELL_COMMAND)
    temp_c = float(system_result.split("=")[1].split("'")[0])
    temp_f = (temp_c * (9.0/5.0)) + 32
    return {
        'temp_c': round(temp_c, 2),
        'temp_f': round(temp_f, 2)
    }


def main():

	system_temp = get_system_temp()

	try:
		Thread(target=json_post, args=(config['system_data_url'], system_temp)).start()
	except KeyError:
		log_config_error("'system_data_url' is not defined in 'config.yml'")



if __name__ == '__main__':
	main()
