import common
import json
import datetime


def getLatLng(location):
    response = common.httpGet('https://www.mapquestapi.com/geocoding/v1/address', {'key': 'kuSBVN6Ik9UUCUYy9SLoIBAoVGxBTtU9',
                                                                                    'inFormat': 'kvp',
                                                                                    'outFormat': 'json',
                                                                                    'location': 'Đại Học FPT',
                                                                                    'thumbMaps': False,
                                                                                    'maxResults': 1})
    data = json.loads(response.text)
    data = data['results'][0]['locations'][0]['latLng']
    print(data)
    obj = {
        'lat': data['lat'],
        'lng': data['lng']
    }
    return obj
