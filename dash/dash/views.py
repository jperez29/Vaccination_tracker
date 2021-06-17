from django.shortcuts import render
from django.shortcuts import HttpResponse
import pandas as pd
import json
from .read_data import read_vacc, read_total

df = read_vacc()
df2 = read_total()

def index(request):
    data = {'data': 'Hello World'}
    return render(request, 'base.html')

def vac_table(request):
    json_records = df.iloc[:125].reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'table_1.html', context)

def total_table(request):
    json_records = df2.iloc[:125].reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'table_2.html', context)


def vac_api(request):
    json_records = df.reset_index().to_json(orient ='records')
    return HttpResponse(json_records)


