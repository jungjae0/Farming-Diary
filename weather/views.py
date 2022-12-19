import urllib
from urllib.parse import quote_plus, urlencode
from urllib.request import urlopen

import orjson
from django.shortcuts import render

from .models import Information

from collections import OrderedDict
from fusioncharts import FusionCharts

import time
import pandas as pd
from datetime import date, timedelta

# def tavg(request):
#     now = time
#     if now.localtime().tm_hour < 11:
#         c_year = date.today() - timedelta(2)
#         l_year = date.today() - timedelta(367)
#     else:
#         c_year = date.today() - timedelta(1)
#         l_year = date.today() - timedelta(366)
#
#     dataSource = OrderedDict()
#
#     df = pd.DataFrame(list(Information.objects.all().values()))
#
#     for i in range(1, 5):
#         df.iloc[:,-i] = pd.to_numeric(df.iloc[:,-i], errors='coerce')
#
#
#     chartConfig = OrderedDict()
#
#     dataSource["chart"] = chartConfig
#     dataSource["data"] = []
#
#     today_tavg = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['tavg'].item()
#     yesterday_tavg = df[df['date'] == f"{l_year.strftime('%Y-%m-%d')}"]['tavg'].item()
#     dataSource["data"].append({"label": '작년', "value": today_tavg})
#     dataSource["data"].append({"label": '올해', "value": yesterday_tavg})
#
#     chartConfig["caption"] = "작년 날씨와 최근 날씨 비교(최근 30일)"
#     if today_tavg < yesterday_tavg:
#         chartConfig["subCaption"] = f"1년 전 대비{round(-(today_tavg - yesterday_tavg),3)}°C증가"
#     elif today_tavg == yesterday_tavg:
#         chartConfig["subCaption"] = f"1년 전과 다른 게 없음"
#     else:
#         chartConfig["subCaption"] = f"1년 전 대비{round(today_tavg - yesterday_tavg, 3)}°C증가"
#
#     chartConfig["numberSuffix"] = "°C"
#     chartConfig["theme"] = "fusion"
#
#     print(c_year.strftime('%Y-%m-%d'))
#     print(l_year.strftime('%Y-%m-%d'))
#     column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)
#
#     # now = time
#     # if now.localtime().tm_hour < 11:
#     #     c_year = date.today() - timedelta(2)
#     # else:
#     #     c_year = date.today() - timedelta(1)
#     #
#     # df = pd.DataFrame(list(Information.objects.all().values()))
#     # for i in range(1, 5):
#     #     df.iloc[:, -i] = pd.to_numeric(df.iloc[:, -i], errors='coerce')
#
#     today_tavg = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['tavg'].item()
#     today_thum = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['thum'].item()
#     today_trainfall = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['rainfall'].item()
#     today_sunshine = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['insolation'].item()
#
#     context = {
#         'yesterday_tavg': today_tavg,
#         'yesterday_thum': today_thum,
#         'yesterday_rainfall': today_trainfall,
#         'yesterday_sunshine': today_sunshine,
#         'output': column2D.render()
#     }
#
#     return render(request, 'weather/temperature.html', context)
#
#
# def thum(request):
#     now = time
#     if now.localtime().tm_hour < 11:
#         c_year = date.today() - timedelta(2)
#         l_year = date.today() - timedelta(367)
#     else:
#         c_year = date.today() - timedelta(1)
#         l_year = date.today() - timedelta(366)
#
#     dataSource = OrderedDict()
#
#     df = pd.DataFrame(list(Information.objects.all().values()))
#     for i in range(1, 5):
#         df.iloc[:, -i] = pd.to_numeric(df.iloc[:, -i], errors='coerce')
#
#     # print(df.head())
#     # print(df.dtypes)
#
#     chartConfig = OrderedDict()
#
#     dataSource["chart"] = chartConfig
#     dataSource["data"] = []
#
#     today_thum = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['thum'].item()
#     yesterday_thum = df[df['date'] == f"{l_year.strftime('%Y-%m-%d')}"]['thum'].item()
#     dataSource["data"].append({"label": '작년', "value": today_thum})
#     dataSource["data"].append({"label": '올해', "value": yesterday_thum})
#
#     chartConfig["caption"] = "작년 습도와 현재 습도 비교"
#     if today_thum < yesterday_thum:
#         chartConfig["subCaption"] = f"1년 전 대비{round(-(today_thum - yesterday_thum),3)}% 증가"
#     elif today_thum == yesterday_thum:
#         chartConfig["subCaption"] = f"1년 전과 다른 게 없음"
#     else:
#         chartConfig["subCaption"] = f"1년 전 대비{round(today_thum - yesterday_thum, 3)}% 감소"
#     chartConfig["numberSuffix"] = "%"
#     chartConfig["theme"] = "fusion"
#
#     column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)
#
#     today_tavg = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['tavg'].item()
#     today_thum = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['thum'].item()
#     today_trainfall = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['rainfall'].item()
#     today_sunshine = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['insolation'].item()
#
#     context = {
#         'yesterday_tavg': today_tavg,
#         'yesterday_thum': today_thum,
#         'yesterday_rainfall': today_trainfall,
#         'yesterday_sunshine': today_sunshine,
#         'output': column2D.render()
#     }
#
#
#     return render(request, 'weather/humid.html', context)
#
# def trainfall(request):
#     now = time
#     if now.localtime().tm_hour < 11:
#         c_year = date.today() - timedelta(2)
#         l_year = date.today() - timedelta(367)
#     else:
#         c_year = date.today() - timedelta(1)
#         l_year = date.today() - timedelta(366)
#
#     dataSource = OrderedDict()
#
#     df = pd.DataFrame(list(Information.objects.all().values()))
#     for i in range(1, 5):
#         df.iloc[:, -i] = pd.to_numeric(df.iloc[:, -i], errors='coerce')
#
#     # print(df.head())
#     # print(df.dtypes)
#
#     chartConfig = OrderedDict()
#
#     dataSource["chart"] = chartConfig
#     dataSource["data"] = []
#
#     today_trainfall = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['rainfall'].item()
#     yesterday_trainfall = df[df['date'] == f"{l_year.strftime('%Y-%m-%d')}"]['rainfall'].item()
#     dataSource["data"].append({"label": '작년', "value": today_trainfall})
#     dataSource["data"].append({"label": '올해', "value": yesterday_trainfall})
#
#     chartConfig["caption"] = "작년 강수량과 현재 강수량 비교"
#     if today_trainfall < yesterday_trainfall:
#         chartConfig["subCaption"] = f"1년 전 대비{round(-(today_trainfall - yesterday_trainfall),3)}mm 증가"
#     elif today_trainfall == yesterday_trainfall:
#         chartConfig["subCaption"] = f"1년 전과 변화 없음"
#     else:
#         chartConfig["subCaption"] = f"1년 전 대비{round(today_trainfall - yesterday_trainfall, 3)}mm 감소"
#     chartConfig["numberSuffix"] = "mm"
#     chartConfig["theme"] = "fusion"
#
#     column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)
#
#     today_tavg = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['tavg'].item()
#     today_thum = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['thum'].item()
#     today_trainfall = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['rainfall'].item()
#     today_sunshine = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['insolation'].item()
#
#     context = {
#         'yesterday_tavg': today_tavg,
#         'yesterday_thum': today_thum,
#         'yesterday_rainfall': today_trainfall,
#         'yesterday_sunshine': today_sunshine,
#         'output': column2D.render()
#     }
#
#     return render(request, 'weather/rainfall.html', context)
#
# def sunshine(request):
#     now = time
#     if now.localtime().tm_hour < 11:
#         c_year = date.today() - timedelta(2)
#         l_year = date.today() - timedelta(367)
#     else:
#         c_year = date.today() - timedelta(1)
#         l_year = date.today() - timedelta(366)
#
#     dataSource = OrderedDict()
#
#     df = pd.DataFrame(list(Information.objects.all().values()))
#     for i in range(1, 5):
#         df.iloc[:, -i] = pd.to_numeric(df.iloc[:, -i], errors='coerce')
#
#     # print(df.head())
#     # print(df.dtypes)
#
#     chartConfig = OrderedDict()
#
#     dataSource["chart"] = chartConfig
#     dataSource["data"] = []
#
#     today_sunshine = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['insolation'].item()
#     yesterday_sunshine = df[df['date'] == f"{l_year.strftime('%Y-%m-%d')}"]['insolation'].item()
#     dataSource["data"].append({"label": '작년', "value": today_sunshine})
#     dataSource["data"].append({"label": '올해', "value": yesterday_sunshine})
#
#     chartConfig["caption"] = "작년 일조량과 현재 일조량 비교"
#     if today_sunshine < yesterday_sunshine:
#         chartConfig["subCaption"] = f"1년 전 대비{round(-(today_sunshine - yesterday_sunshine),3)}MJ/cm2 증가"
#     elif today_sunshine == yesterday_sunshine:
#         chartConfig["subCaption"] = f"1년 전과 변화 없음"
#     else:
#         chartConfig["subCaption"] = f"1년 전 대비{today_sunshine - yesterday_sunshine}J/cm2 감소"
#     chartConfig["numberSuffix"] = "MJ/cm2"
#     chartConfig["theme"] = "fusion"
#
#     column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)
#
#     today_tavg = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['tavg'].item()
#     today_thum = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['thum'].item()
#     today_trainfall = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['rainfall'].item()
#     today_sunshine = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['insolation'].item()
#
#     context = {
#         'yesterday_tavg': today_tavg,
#         'yesterday_thum': today_thum,
#         'yesterday_rainfall': today_trainfall,
#         'yesterday_sunshine': today_sunshine,
#         'output': column2D.render()
#     }
#
#     return render(request, 'weather/sunshine.html', context)


# def yesterday_weather(request):
#
#     now = time
#     if now.localtime().tm_hour < 11:
#         c_year = date.today() - timedelta(2)
#     else:
#         c_year = date.today() - timedelta(1)
#
#     df = pd.DataFrame(list(Information.objects.all().values()))
#     for i in range(1, 5):
#         df.iloc[:, -i] = pd.to_numeric(df.iloc[:, -i], errors='coerce')
#
#     today_tavg = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['tavg'].item()
#     today_thum = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['thum'].item()
#     today_trainfall = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['rainfall'].item()
#     today_sunshine = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['insolation'].item()
#
#     context = {
#         'yesterday_tavg': today_tavg,
#         'yesterday_thum': today_thum,
#         'yesterday_rainfall': today_trainfall,
#         'yesterday_sunshine': today_sunshine,
#     }
#
#     return render(request, 'weather/yesterday-weather.html', context)


def tavg(request):
    url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
    servicekey = 'HOhrXN4295f2VXKpOJc4gvpLkBPC/i97uWk8PfrUIONlI7vRB9ij088/F5RvIjZSz/PUFjJ4zkMjuBkbtMHqUg=='

    now = time
    if now.localtime().tm_hour < 11:
        c_year = (date.today() - timedelta(2)).strftime("%Y%m%d")
        l_year = (date.today() - timedelta(367)).strftime("%Y%m%d")

    else:
        c_year = (date.today() - timedelta(1)).strftime("%Y%m%d")
        l_year = (date.today() - timedelta(366)).strftime("%Y%m%d")


    dataSource = OrderedDict()

    params = f'?{quote_plus("ServiceKey")}={servicekey}&' + urlencode({
        quote_plus("pageNo"): "1", # 페이지 번호 // default : 1
        quote_plus("numOfRows"): "720", # 한 페이지 결과 수 // default : 10
        quote_plus("dataType"): "JSON", # 응답자료형식 : XML, JSON
        quote_plus("dataCd"): "ASOS",
        quote_plus("dateCd"): "DAY",
        quote_plus("startDt"): f"{l_year}",
        quote_plus("endDt"): f"{c_year}",
        quote_plus("stnIds"): "108"
        })

    req = urllib.request.Request(url + params)

    response_body = urlopen(req).read()

    data = orjson.loads(response_body)

    s_res = data['response']['body']['items']['item'][0]
    e_res = data['response']['body']['items']['item'][-1]

    c_tavg = e_res['avgTa']
    l_tavg = s_res['avgTa']

    if c_tavg == '':
        c_tavg = int(0)
    else:
        c_tavg = float(e_res['avgTa'])

    if l_tavg == '':
        l_tavg = int(0)
    else:
        l_tavg = float(s_res['avgTa'])

    dataSource = OrderedDict()

    chartConfig = OrderedDict()
    chartConfig["caption"] = "작년 VS 올해 : 온도"
    if l_tavg > c_tavg:
        chartConfig["subCaption"] = f"1년 전 오늘 대비 {round(c_tavg - l_tavg, 3)}°C 감소"
    elif l_tavg == c_tavg:
        chartConfig["subCaption"] = f"1년 전 오늘과 평균 온도 같음"
    else:
        chartConfig["subCaption"] = f"1년 전 오늘 대비 {round(c_tavg - l_tavg, 3)}°C 증가"

    chartConfig["numberSuffix"] = "°C"
    chartConfig["theme"] = "fusion"

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    dataSource["data"].append({"label" : '작년', "value": l_tavg})
    dataSource["data"].append({"label" : '올해', "value": c_tavg})


    column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)

    context = {
        'output': column2D.render(),
        'tavg': e_res['avgTa'],
        'thum': e_res['avgRhm'],
        'rain': e_res['sumRn'],
        'sun': e_res['sumGsr']

    }

    return render(request, 'weather/temperature.html', context)

def thum(request):
    url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
    servicekey = 'HOhrXN4295f2VXKpOJc4gvpLkBPC/i97uWk8PfrUIONlI7vRB9ij088/F5RvIjZSz/PUFjJ4zkMjuBkbtMHqUg=='

    now = time
    if now.localtime().tm_hour < 11:
        c_year = (date.today() - timedelta(2)).strftime("%Y%m%d")
        l_year = (date.today() - timedelta(367)).strftime("%Y%m%d")

    else:
        c_year = (date.today() - timedelta(1)).strftime("%Y%m%d")
        l_year = (date.today() - timedelta(366)).strftime("%Y%m%d")


    dataSource = OrderedDict()

    params = f'?{quote_plus("ServiceKey")}={servicekey}&' + urlencode({
        quote_plus("pageNo"): "1", # 페이지 번호 // default : 1
        quote_plus("numOfRows"): "720", # 한 페이지 결과 수 // default : 10
        quote_plus("dataType"): "JSON", # 응답자료형식 : XML, JSON
        quote_plus("dataCd"): "ASOS",
        quote_plus("dateCd"): "DAY",
        quote_plus("startDt"): f"{l_year}",
        quote_plus("endDt"): f"{c_year}",
        quote_plus("stnIds"): "108"
        })

    req = urllib.request.Request(url + params)

    response_body = urlopen(req).read()

    data = orjson.loads(response_body)

    s_res = data['response']['body']['items']['item'][0]
    e_res = data['response']['body']['items']['item'][-1]

    c_thum = e_res['avgRhm']
    l_thum = s_res['avgRhm']

    if c_thum == '':
        c_thum = int(0)
    else:
        c_thum = float(e_res['avgRhm'])

    if l_thum == '':
        l_thum = int(0)
    else:
        l_thum = float(s_res['avgRhm'])

    dataSource = OrderedDict()

    chartConfig = OrderedDict()
    chartConfig["caption"] = "작년 VS 올해 : 습도"
    if l_thum > c_thum:
        chartConfig["subCaption"] = f"1년 전 오늘 대비 {round(c_thum - l_thum, 3)}% 감소"
    elif l_thum == c_thum:
        chartConfig["subCaption"] = "1년 전과 습도 같음"
    else:
        chartConfig["subCaption"] = f"1년 전 오늘 대비 {round(c_thum - l_thum, 3)}% 증가"

    chartConfig["numberSuffix"] = "*"
    chartConfig["theme"] = "fusion"

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    dataSource["data"].append({"label" : '작년', "value": l_thum})
    dataSource["data"].append({"label" : '올해', "value": c_thum})

    column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)

    context = {
        'output': column2D.render(),
        'tavg': e_res['avgTa'],
        'thum': e_res['avgRhm'],
        'rain': e_res['sumRn'],
        'sun': e_res['sumGsr']
    }

    return render(request, 'weather/humid.html', context)


def trainfall(request):
    url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
    servicekey = 'HOhrXN4295f2VXKpOJc4gvpLkBPC/i97uWk8PfrUIONlI7vRB9ij088/F5RvIjZSz/PUFjJ4zkMjuBkbtMHqUg=='

    now = time
    if now.localtime().tm_hour < 11:
        c_year = (date.today() - timedelta(2)).strftime("%Y%m%d")
        l_year = (date.today() - timedelta(367)).strftime("%Y%m%d")

    else:
        c_year = (date.today() - timedelta(1)).strftime("%Y%m%d")
        l_year = (date.today() - timedelta(366)).strftime("%Y%m%d")


    dataSource = OrderedDict()

    params = f'?{quote_plus("ServiceKey")}={servicekey}&' + urlencode({
        quote_plus("pageNo"): "1", # 페이지 번호 // default : 1
        quote_plus("numOfRows"): "720", # 한 페이지 결과 수 // default : 10
        quote_plus("dataType"): "JSON", # 응답자료형식 : XML, JSON
        quote_plus("dataCd"): "ASOS",
        quote_plus("dateCd"): "DAY",
        quote_plus("startDt"): f"{l_year}",
        quote_plus("endDt"): f"{c_year}",
        quote_plus("stnIds"): "108"
        })

    req = urllib.request.Request(url + params)

    response_body = urlopen(req).read()

    data = orjson.loads(response_body)

    all = data['response']['body']['items']['item']
    s_res = data['response']['body']['items']['item'][0]
    e_res = data['response']['body']['items']['item'][-1]


    c_rain = e_res['sumRn']
    l_rain = s_res['sumRn']

    if c_rain == '':
        c_rain = int(0)
    else:
        c_rain = float(e_res['sumRn'])

    if l_rain == '':
        l_rain = int(0)
    else:
        l_rain = float(s_res['sumRn'])

    # print(type(c_rain))

    dataSource = OrderedDict()

    chartConfig = OrderedDict()
    chartConfig["caption"] = "작년 VS 올해 : 강수량"
    if l_rain > c_rain:
        chartConfig["subCaption"] = f"1년 전 오늘 대비 {round(float(c_rain) - float(l_rain), 3)}mm 감소"
    elif l_rain == c_rain:
        chartConfig["subCaption"] = "1년 전과 강수량 같음"
    else:
        chartConfig["subCaption"] = f"1년 전 오늘 대비 {round(float(c_rain) - float(l_rain), 3)}mm 증가"

    chartConfig["numberSuffix"] = "mm"
    chartConfig["theme"] = "fusion"

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    dataSource["data"].append({"label" : '작년', "value": l_rain})
    dataSource["data"].append({"label" : '올해', "value": c_rain})

    column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)

    context = {
        'output': column2D.render(),
        'tavg': e_res['avgTa'],
        'thum': e_res['avgRhm'],
        'rain': e_res['sumRn'],
        'sun': e_res['sumGsr']

    }

    return render(request, 'weather/rainfall.html', context)


def sunshine(request):
    url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
    servicekey = 'HOhrXN4295f2VXKpOJc4gvpLkBPC/i97uWk8PfrUIONlI7vRB9ij088/F5RvIjZSz/PUFjJ4zkMjuBkbtMHqUg=='

    now = time
    if now.localtime().tm_hour < 11:
        c_year = (date.today() - timedelta(2)).strftime("%Y%m%d")
        l_year = (date.today() - timedelta(367)).strftime("%Y%m%d")

    else:
        c_year = (date.today() - timedelta(1)).strftime("%Y%m%d")
        l_year = (date.today() - timedelta(366)).strftime("%Y%m%d")


    dataSource = OrderedDict()

    params = f'?{quote_plus("ServiceKey")}={servicekey}&' + urlencode({
        quote_plus("pageNo"): "1", # 페이지 번호 // default : 1
        quote_plus("numOfRows"): "720", # 한 페이지 결과 수 // default : 10
        quote_plus("dataType"): "JSON", # 응답자료형식 : XML, JSON
        quote_plus("dataCd"): "ASOS",
        quote_plus("dateCd"): "DAY",
        quote_plus("startDt"): f"{l_year}",
        quote_plus("endDt"): f"{c_year}",
        quote_plus("stnIds"): "108"
        })

    req = urllib.request.Request(url + params)

    response_body = urlopen(req).read()

    data = orjson.loads(response_body)

    # 작년
    s_res = data['response']['body']['items']['item'][0]
    # 올해
    e_res = data['response']['body']['items']['item'][-1]

    c_sun = e_res['sumGsr']
    l_sun = s_res['sumGsr']

    if c_sun == '':
        c_sun = int(0)
    else:
        c_sun = float(e_res['sumGsr'])

    if l_sun == '':
        l_sun = int(0)
    else:
        l_sun = float(s_res['sumGsr'])

    print(s_res['tm'])
    print(s_res['sumGsr'])

    dataSource = OrderedDict()

    chartConfig = OrderedDict()
    chartConfig["caption"] = "작년 VS 올해 : 일사량"
    if l_sun > c_sun:
        chartConfig["subCaption"] = f"1년 전 오늘 대비 {round(float(c_sun) - float(l_sun), 3)} MJ/cm2 감소"
    elif l_sun == c_sun:
        chartConfig["subCaption"] = f"1년 전과 일사량 같음"
    else:
        chartConfig["subCaption"] = f"1년 전 오늘 대비 {round(float(c_sun) - float(l_sun), 3)} MJ/cm2 증가"

    chartConfig["numberSuffix"] = "MJ/cm2"
    chartConfig["theme"] = "fusion"

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    dataSource["data"].append({"label" : '작년', "value": l_sun})
    dataSource["data"].append({"label" : '올해', "value": c_sun})

    column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)

    context = {
        'output': column2D.render(),
        'tavg': e_res['avgTa'],
        'thum': e_res['avgRhm'],
        'rain': e_res['sumRn'],
        'sun': e_res['sumGsr']
    }

    return render(request, 'weather/sunshine.html', context)