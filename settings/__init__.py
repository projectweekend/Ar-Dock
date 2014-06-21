import yaml


with open('./config.yml') as file_data:
    config = yaml.safe_load(file_data)
    sensors_config = config['sensors']
