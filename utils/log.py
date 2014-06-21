import logging
from datetime import datetime


def log_post_error(status_code, response_body):
    entry_template = '{0}: {1} - "{2}"'
    log_time = datetime.now()
    logging.info(entry_template.format(log_time, status_code, response_body))


def log_config_error(message):
    entry_template = '{0}: Config - "{1}"'
    log_time = datetime.now()
    logging.info(entry_template.format(log_time, message))
