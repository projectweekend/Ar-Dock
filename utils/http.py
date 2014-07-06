import os
import json
import requests
from .log import log_post_error

AUTH_TOKEN = os.getenv('AUTH_TOKEN', '')


def json_post(url, data):

    headers = {
        'content-type': 'application/json'
    }

    if AUTH_TOKEN:
        headers['authorization'] = "Bearer {0}".format(AUTH_TOKEN)

    data = json.dumps(data)

    response = requests.post(url, data=data, headers=headers)
    if response.status_code != requests.codes.created:
        log_post_error(response.status_code, response.json())
