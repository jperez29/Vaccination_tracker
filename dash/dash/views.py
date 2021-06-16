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
    json_records = df.iloc[:125].reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'table_1.html', context)

def vac_api(request):
    json_records = df.reset_index().to_json(orient ='records')
    return HttpResponse(json_records)


