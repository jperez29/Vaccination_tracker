from django.shortcuts import render
from django.shortcuts import HttpResponse
import pandas as pd
import json
from .read_data import read_df

df= read_df()

def index(request):
    data = {'data': 'Hello World'}
    return render(request, 'base.html')

def vac_table(request):
    json_records = df.to_json(orient="split")
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    print(type(context['d']['data']))
  
    # return render(request, 'table_1.html', context)
    # data = df.to_json(orient="split")
    return HttpResponse(context['d']['data'])
