import urllib
from urllib.parse import quote_plus, urlencode
from urllib.request import urlopen
import orjson
import os
import schedule
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eventcalendar.settings")

import django
django.setup()

from weather.models import Information

def parser():
    url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
    servicekey = 'HOhrXN4295f2VXKpOJc4gvpLkBPC/i97uWk8PfrUIONlI7vRB9ij088/F5RvIjZSz/PUFjJ4zkMjuBkbtMHqUg=='

    # 전날 자료까지만 제공

    sday = 20221208
    eday = 20221208

    params = f'?{quote_plus("ServiceKey")}={servicekey}&' + urlencode({
        quote_plus("pageNo"): "1",  # 페이지 번호 // default : 1
        quote_plus("numOfRows"): "720",  # 한 페이지 결과 수 // default : 10
        quote_plus("dataType"): "JSON",  # 응답자료형식 : XML, JSON
        quote_plus("dataCd"): "ASOS",
        quote_plus("dateCd"): "DAY",
        quote_plus("startDt"): f"{sday}",
        quote_plus("endDt"): f"{eday}",
        quote_plus("stnIds"): "108"
    })

    req = urllib.request.Request(url + params)

    response_body = urlopen(req).read()

    data = orjson.loads(response_body)
    print(data)

    weather_data = data['response']['body']['items']['item']

    result = []
    for weather in weather_data:
        stnId = weather['stnId']
        stnNm = weather['stnNm']
        date = weather['tm']
        if weather['avgTa'] != '':
            tavg = weather['avgTa']
        else:
            tavg = 'none'
        if weather['avgRhm'] != '':
            thum = weather['avgRhm']
        else:
            thum = 'none'
        if weather['sumRn'] != '':
            rainfall = weather['sumRn']
        else:
            rainfall = ''
        if weather['sumGsr'] != '':
            insolation = weather['sumGsr']
        else:
            insolation = 'none'

        data = {
            'stnId':stnId,
            'stnNm': stnNm,
            'date': date,
            'tavg': tavg,
            'thum': thum,
            'rainfall': rainfall,
            'insolation': insolation,
        }
        result.append(data)

    return result

if __name__ == '__main__':
    data = parser()
    for item in data:
        Information(
            stnId = item['stnId'],
            stnNm = item['stnNm'],
            date = item['date'],
            tavg = item['tavg'],
            thum = item['thum'],
            rainfall = item['rainfall'],
            insolation=item['insolation'],
                    ).save()




