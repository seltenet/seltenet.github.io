# get data from https://114.selte.net/jeecg-boot/sys/common/static/city.json

import json
import requests

url = 'https://114.selte.net/jeecg-boot/sys/common/static/city.json'
r = requests.get(url)
data = json.loads(r.text)


def get_city(city):
    for i in data:
        if i['name'] == city:
            return i['code']
    return None

#