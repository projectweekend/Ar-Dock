import json
import requests
from .log import log_post_error


def json_post(url, data):

    headers = {'content-type': 'application/json'}
    data = json.dumps(data)

    response = requests.post(url, data=data, headers=headers)
    if response.status_code != requests.codes.created:
        log_post_error(response.status_code, response.json())
