def parse_sensor_data(sensor_data_string):
    readings = dict([p.split(':') for p in sensor_data_string.split('|')])
    for k, v in readings.items():
        readings[k] = float(v)
    return readings
