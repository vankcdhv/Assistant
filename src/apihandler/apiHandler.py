from youtube_search import YoutubeSearch
import common
import json
import datetime
from .location import *
import wikipedia


def getWeather(input):
    inp = input.lower().split(' | ')
    time = inp[1]
    locationName = inp[2]
    latlng = getLatLng(locationName)
    option = {
        'lat': latlng['lat'],
        'lon': latlng['lng'],
        'exclude': 'hourly',
        'appid': 'c8d9c1623804964c00484cb76f23324a',
        'lang': 'vi',
        'units': 'metric',
    }
    response = common.httpGet(
        'https://api.openweathermap.org/data/2.5/onecall', option)
    data = json.loads(response.text)
    if((''+time).strip() == 'hôm nay'):
        obj = {
            "temp": data['daily'][0]['temp']['eve'],
            "weather": data['daily'][0]['weather'][0]['description']
        }
        result = 'Thời tiết tại ' + locationName + ' ' + time + \
            ' nhiệt độ ' + str(obj['temp']) + ' độ có ' + obj['weather']
        return result
    if((''+time).strip() == 'ngày mai'):
        obj = {
            "temp": data['daily'][1]['temp']['eve'],
            "weather": data['daily'][1]['weather'][0]['description']
        }
        result = 'Thời tiết tại ' + locationName + ' ' + time + \
            ' nhiệt độ ' + str(obj['temp']) + ' độ có ' + obj['weather']
        return result
    if((''+time).strip() == 'bây giờ'):
        data = data['current']
        obj = {
            "temp": data['temp'],
            "weather": data['weather'][0]['description']
        }
        result = 'Thời tiết tại ' + locationName + ' ' + time + \
            ' nhiệt độ ' + str(obj['temp']) + ' độ có ' + obj['weather']
        return result


def youtube(name):
    results = YoutubeSearch(name, max_results=1).to_dict()
    if(len(results) > 0):
        url = 'https://www.youtube.com'+results[0]['url_suffix']
    else:
        url = None
    return url
def wikipedia_sumary(key_word):
    wikipedia.set_lang('vi')
    return wikipedia.summary(key_word)
