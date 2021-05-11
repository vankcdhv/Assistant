import requests
import json

def httpGet(url, params):
    result = requests.get(url, params=params)
    return result


