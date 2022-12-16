import json
import urllib
import warnings
from urllib.parse import quote_plus, urlencode
from urllib.request import urlopen
import pandas as pd
import orjson
from django.shortcuts import render
from django.http import HttpResponse

from collections import OrderedDict
from fusioncharts import FusionCharts

from .models import Information

import requests
from datetime import date, timedelta

def tavg(request):

    c_year = date.today() - timedelta(1)
    l_year = date.today() - timedelta(366)

    dataSource = OrderedDict()

    df = pd.DataFrame(list(Information.objects.all().values()))

    for i in range(1, 5):
        df.iloc[:,-i] = pd.to_numeric(df.iloc[:,-i], errors='coerce')

    # print(df.head())
    # print(df.dtypes)

    chartConfig = OrderedDict()

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    today_tavg = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['tavg'].item()
    yesterday_tavg = df[df['date'] == f"{l_year.strftime('%Y-%m-%d')}"]['tavg'].item()
    dataSource["data"].append({"label": '작년', "value": today_tavg})
    dataSource["data"].append({"label": '올해', "value": yesterday_tavg})

    chartConfig["caption"] = "작년 날씨와 최근 날씨 비교(최근 30일)"
    if today_tavg < yesterday_tavg:
        chartConfig["subCaption"] = f"1년 전 대비{round(-(today_tavg - yesterday_tavg),3)}°C증가"
    elif today_tavg == yesterday_tavg:
        chartConfig["subCaption"] = f"1년 전과 다른 게 없음"
    else:
        chartConfig["subCaption"] = f"1년 전 대비{round(today_tavg - yesterday_tavg, 3)}°C증가"

    chartConfig["numberSuffix"] = "°C"
    chartConfig["theme"] = "fusion"

    print(c_year.strftime('%Y-%m-%d'))
    print(l_year.strftime('%Y-%m-%d'))
    column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)
    return render(request, 'weather/temperature.html', {
     'output': column2D.render()
    })


def thum(request):

    c_year = date.today() - timedelta(1)
    l_year = date.today() - timedelta(366)

    dataSource = OrderedDict()

    df = pd.DataFrame(list(Information.objects.all().values()))
    for i in range(1, 5):
        df.iloc[:, -i] = pd.to_numeric(df.iloc[:, -i], errors='coerce')

    # print(df.head())
    # print(df.dtypes)

    chartConfig = OrderedDict()

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    today_thum = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['thum'].item()
    yesterday_thum = df[df['date'] == f"{l_year.strftime('%Y-%m-%d')}"]['thum'].item()
    dataSource["data"].append({"label": '작년', "value": today_thum})
    dataSource["data"].append({"label": '올해', "value": yesterday_thum})

    chartConfig["caption"] = "작년 습도와 현재 습도 비교"
    if today_thum < yesterday_thum:
        chartConfig["subCaption"] = f"1년 전 대비{round(-(today_thum - yesterday_thum),3)}% 증가"
    elif today_thum == yesterday_thum:
        chartConfig["subCaption"] = f"1년 전과 다른 게 없음"
    else:
        chartConfig["subCaption"] = f"1년 전 대비{round(today_thum - yesterday_thum, 3)}% 감소"
    chartConfig["numberSuffix"] = "%"
    chartConfig["theme"] = "fusion"

    column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)
    return render(request, 'weather/humid.html', {
        'output': column2D.render()
    })

def trainfall(request):

    c_year = date.today() - timedelta(1)
    l_year = date.today() - timedelta(366)

    dataSource = OrderedDict()

    df = pd.DataFrame(list(Information.objects.all().values()))
    for i in range(1, 5):
        df.iloc[:, -i] = pd.to_numeric(df.iloc[:, -i], errors='coerce')

    # print(df.head())
    # print(df.dtypes)

    chartConfig = OrderedDict()

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    today_trainfall = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['rainfall'].item()
    yesterday_trainfall = df[df['date'] == f"{l_year.strftime('%Y-%m-%d')}"]['rainfall'].item()
    dataSource["data"].append({"label": '작년', "value": today_trainfall})
    dataSource["data"].append({"label": '올해', "value": yesterday_trainfall})

    chartConfig["caption"] = "작년 강우량과 현재 강우량 비교"
    if today_trainfall < yesterday_trainfall:
        chartConfig["subCaption"] = f"1년 전 대비{round(-(today_trainfall - yesterday_trainfall),3)}mm 증가"
    elif today_trainfall == yesterday_trainfall:
        chartConfig["subCaption"] = f"1년 전과 변화 없음"
    else:
        chartConfig["subCaption"] = f"1년 전 대비{round(today_trainfall - yesterday_trainfall, 3)}mm 감소"
    chartConfig["numberSuffix"] = "mm"
    chartConfig["theme"] = "fusion"

    column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)
    return render(request, 'weather/rainfall.html', {
        'output': column2D.render()
    })

def sunshine(request):

    c_year = date.today() - timedelta(1)
    l_year = date.today() - timedelta(366)

    dataSource = OrderedDict()

    df = pd.DataFrame(list(Information.objects.all().values()))
    for i in range(1, 5):
        df.iloc[:, -i] = pd.to_numeric(df.iloc[:, -i], errors='coerce')

    # print(df.head())
    # print(df.dtypes)

    chartConfig = OrderedDict()

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    today_sunshine = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['insolation'].item()
    yesterday_sunshine = df[df['date'] == f"{l_year.strftime('%Y-%m-%d')}"]['insolation'].item()
    dataSource["data"].append({"label": '작년', "value": today_sunshine})
    dataSource["data"].append({"label": '올해', "value": yesterday_sunshine})

    chartConfig["caption"] = "작년 일조량과 현재 일조량 비교"
    if today_sunshine < yesterday_sunshine:
        chartConfig["subCaption"] = f"1년 전 대비{round(-(today_sunshine - yesterday_sunshine),3)}MJ/cm2 증가"
    elif today_sunshine == yesterday_sunshine:
        chartConfig["subCaption"] = f"1년 전과 변화 없음"
    else:
        chartConfig["subCaption"] = f"1년 전 대비{today_sunshine - yesterday_sunshine}J/cm2 감소"
    chartConfig["numberSuffix"] = "MJ/cm2"
    chartConfig["theme"] = "fusion"

    column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)
    return render(request, 'weather/yesterday-weather.html', {
        'output': column2D.render()
    })


def yesterday_weather(request):

    c_year = date.today() - timedelta(1)

    df = pd.DataFrame(list(Information.objects.all().values()))
    for i in range(1, 5):
        df.iloc[:, -i] = pd.to_numeric(df.iloc[:, -i], errors='coerce')

    today_tavg = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['tavg'].item()
    today_thum = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['thum'].item()
    today_trainfall = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['rainfall'].item()
    today_sunshine = df[df['date'] == f"{c_year.strftime('%Y-%m-%d')}"]['insolation'].item()

    context = {
        'yesterday_tavg': today_tavg,
        'yesterday_thum': today_thum,
        'yesterday_rainfall': today_trainfall,
        'yesterday_sunshine': today_sunshine,
    }

    return render(request, 'weather/yesterday-weather.html', context)
