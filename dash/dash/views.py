from django.shortcuts import render
from django.shortcuts import HttpResponse
from .read_data import create_connect, read_vacc, read_total
from .bar_charts import top_states, bottom_states
from .map import state_map
from .line_chart import line_chart_1, line_chart_2,scatter_plot, scatter_plot_2
from bokeh.embed import components
from bokeh.layouts import row,column, gridplot
from bokeh.io import curdoc
import pandas as pd
import numpy as np
import json

df = read_vacc()
df2 = read_total()
df2 = df2.sort_values(by='perc_daily_vacc_pop',ascending=False)
index = [i for i in range(1,len(df2)+1)]
df2['Rank'] = index
# state = 'Alabama'
data = []
vacc_map = state_map()
top = top_states()
bottom = bottom_states()
al_num_vacc = line_chart_1(state = 'Mississippi')
al_perc_vacc = line_chart_2(state = 'Mississippi')
ver_num_vacc = line_chart_1(state = 'Vermont')
ver_perc_vacc = line_chart_2(state = 'Vermont')
scatter = scatter_plot()
scatter_2 = scatter_plot_2()
state_list = df2['location'].tolist()


def vac_table(request):
    grid = gridplot([al_num_vacc, al_perc_vacc, ver_num_vacc, ver_perc_vacc], ncols=2)
    bar_row = gridplot([top,bottom,scatter, scatter_2], ncols=2)
    script, divs = components((bar_row,vacc_map, grid))    
    json_records = df2.to_json(orient='records')
    data = json.loads(json_records)
    context = {'d': data,'div_line': divs[2],'script':script, 'div_bar':divs[0], 'div_map':divs[1]}

    return render(request, 'table_1.html', context)


def vac_api(request):
    json_records = df.reset_index().to_json(orient='records')
    return HttpResponse(json_records)
