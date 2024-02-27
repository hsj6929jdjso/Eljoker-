import requests
import time
import random

data = 'KsK/cJCpbsJAYh9G/GbvdCYtDB4JWXJpc49ULltB7cQ='
header = {
    'Host': 'api.crazylab.app',
    'channel': 'dev',
    'timestamp': '1709009512061',
    'token': 'eyJpZCI6MTE0Njg0MDAsInRva2VuIjoiMWVjMjQ0MTczZmYxYmQ4Mzk0MGQ3YmUxOWEzOGUxOTMifQ',
    'language': 'ar',
    'version': '1.1.3',
    'platform': '1',
    'sign': '95738CB6767BFCECC4BB99B3A0236FCD',
    'content-type': 'application/json; charset=UTF-8',
    'content-length': '44',
    'accept-encoding': 'gzip',
    'user-agent': 'okhttp/4.4.0',
}

while True:
    try:
        url = 'https://api.crazy-hero.net/api/v1/offlineReward'
        r = requests.post(url, headers=header, data=data).text
        print(r)
        sleep_time = random.randint(60, 61)
        print("Sleeping for", sleep_time, "seconds...")
        time.sleep(sleep_time)
        print('')
    except requests.exceptions.RequestException:
        print("No internet connection. Retrying in 10 seconds...")
        time.sleep(10)
        continue