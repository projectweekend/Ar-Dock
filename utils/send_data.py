import os
import json
import requests
import logging
from datetime import datetime


SEND_URL = os.getenv('SEND_URL', 'http://holly.local/api/starbug/sensor')


def log_failure(status_code, response_body):
    entry_template = '{0}: {1} - "{2}"'
    log_time = datetime.now()
    logging.info(entry_template.format(log_time, status_code, response_body))


def json_post(url, data):
    headers = {'content-type': 'application/json'}
    data = json.dumps(data)
    return requests.post(SEND_URL, data=data, headers=headers)


def send_starbug_data(data):
    response = json_post(SEND_URL, data)
    if response.status_code != requests.codes.created:
        log_failure(response.status_code, response.json())
