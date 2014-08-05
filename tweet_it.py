import os
import datetime
import twitter


TWITTER_CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY', '')
TWITTER_CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET', '')
TWITTER_ACCESS_TOKEN_KEY = os.getenv('TWITTER_ACCESS_TOKEN_KEY', '')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET', '')


def main():
    tc = twitter_client()
    sensor_data = read_all_sensors()
    message = temperature_status_message(sensor_data)
    if message:
        tc.PostUpdate(message)


def twitter_client():
    return twitter.Api(consumer_key=TWITTER_CONSUMER_KEY,
                        consumer_secret=TWITTER_CONSUMER_SECRET,
                        access_token_key=TWITTER_ACCESS_TOKEN_KEY,
                        access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

def current_datetime():
    dt = datetime.datetime.now()
    return dt.strftime("%m/%d/%Y - %H:%M")


def read_all_sensors():
    # TODO: make this get temperature reading
    return None


def temperature_status_message(sensor_data):
    message_template = "The current indoor temperature is: {0} F/{1} C ({2}) #raspberrypi"
    try:
        celsius = round(sensor_data['celsius'], 2)
        fahrenheit = round(sensor_data['fahrenheit'], 2)
    except KeyError:
        # TODO: send an email to me
        return
    return message_template.format(fahrenheit, celsius, current_datetime())


if __name__ == '__main__':
    main()
