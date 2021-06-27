from django.shortcuts import render
from django.shortcuts import HttpResponse
from .read_data import create_connect, read_vacc, read_total
from .bar_charts import top_states, bottom_states
from .map import state_map
from .line_chart import line_chart_1, line_chart_2
from bokeh.embed import components
from bokeh.layouts import row,column, gridplot
import pandas as pd
import numpy as np
import json

df = read_vacc()
df2 = read_total()
df2 = df2.sort_values(by='perc_daily_vacc_pop',ascending=False)
index = [i for i in range(1,len(df2)+1)]
df2['Rank'] = index
state = 'Alabama'
data = []
vacc_map = state_map()
top = top_states()
bottom = bottom_states()

num_vacc = line_chart_1(state)
perc_vacc = line_chart_2(state)


# def index(request):
#     data = {'data': 'Hello World'}
#     return render(request, 'base.html')


def vac_table(request):
    c = column(children = [vacc_map, num_vacc,perc_vacc], sizing_mode = 'fixed')
    script_line, div_line = components(c)

    bar_row = row(top,bottom)
    script_bar, div_bar = components(bar_row)    
    json_records = df2.to_json(orient='records')
    data = json.loads(json_records)
    context = {'d': data,'script': script_line, 'div': div_line, 'script_bar':script_bar, 'div_bar':div_bar}
    return render(request, 'table_1.html', context)


def vac_api(request):
    json_records = df.reset_index().to_json(orient='records')
    return HttpResponse(json_records)
