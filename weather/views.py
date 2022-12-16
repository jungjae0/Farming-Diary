import json
import urllib
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
from datetime import date

# print(date.today().strftime('%Y%m%d'))
#
# #

def tavg(request):

    c_year = date.today().strftime('%Y-%m-%d')
    l_year = date.today().strftime('%Y-%m-%d')

    dataSource = OrderedDict()

    df = pd.DataFrame(list(Information.objects.all().values()))
    for i in range(1, 5):
        df.iloc[:,-i] = pd.to_numeric(df.iloc[:,-i], errors='coerce')

    # print(df.head())
    # print(df.dtypes)

    chartConfig = OrderedDict()
    chartConfig["caption"] = "작년 날씨와 최근 날씨 비교"
    chartConfig["subCaption"] = "1년 전 오늘 대비 - 증가"
    chartConfig["numberSuffix"] = "*"
    chartConfig["theme"] = "fusion"

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    today_tavg = df[df['date'] == '2022-11-05']['tavg']
    yesterday_tavg = df[df['date'] == '2022-11-30']['tavg']
    dataSource["data"].append({"label": '작년', "value": today_tavg.item()})
    dataSource["data"].append({"label": '올해', "value": yesterday_tavg.item()})

    column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)
    return render(request, 'weather/temperature.html', {
     'output': column2D.render()
    })


def thum(request):

    c_year = date.today().strftime('%Y-%m-%d')
    l_year = date.today().strftime('%Y-%m-%d')

    dataSource = OrderedDict()

    df = pd.DataFrame(list(Information.objects.all().values()))
    for i in range(1, 5):
        df.iloc[:, -i] = pd.to_numeric(df.iloc[:, -i], errors='coerce')

    # print(df.head())
    # print(df.dtypes)

    chartConfig = OrderedDict()
    chartConfig["caption"] = "작년 습도와 현재 습도 비교"
    chartConfig["subCaption"] = "1년 전 오늘 대비 - 증가"
    chartConfig["numberSuffix"] = "*"
    chartConfig["theme"] = "fusion"

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    today_tavg = df[df['date'] == '2022-11-05']['thum']
    yesterday_tavg = df[df['date'] == '2022-11-30']['thum']
    dataSource["data"].append({"label": '작년', "value": today_tavg.item()})
    dataSource["data"].append({"label": '올해', "value": yesterday_tavg.item()})

    column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)
    return render(request, 'weather/humid.html', {
        'output': column2D.render()
    })