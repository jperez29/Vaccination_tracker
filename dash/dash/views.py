from django.shortcuts import render
from django.shortcuts import HttpResponse
from .read_data import create_connect, read_vacc, read_total
from .bar_charts import top_states, bottom_states
from bokeh.embed import components

import pandas as pd
import json

df = read_vacc()
df2 = read_total()


def index(request):
    data = {'data': 'Hello World'}
    return render(request, 'base.html')


def vac_table(request):
    json_records = df.iloc[:125].reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'table_1.html', context)


def total_table(request):
    json_records = df2.iloc[:125].reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'table_2.html', context)


def vac_api(request):
    json_records = df.reset_index().to_json(orient='records')
    return HttpResponse(json_records)


def chartpath(request):
    p = top_states()
    script, div = components(p)

    return render(request, 'charts.html', {'script': script, 'div': div})
