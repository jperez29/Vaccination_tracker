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
    return HttpResponse(df.to_html())


