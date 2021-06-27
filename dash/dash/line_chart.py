import pandas as pd
import sqlite3 as sql
from bokeh.plotting import figure,show
from bokeh.embed import components
from bokeh.models import ColumnDataSource, HoverTool,Legend
from bokeh.transform import factor_cmap
from .read_data import create_connect,read_vacc, read_total

state = 'Alabama'
def line_chart_1(state):
    total = read_total()
    vacc = read_vacc()
    state_doses   = dict(zip(total.location,total.doses_needed))
   
    new_vacc = vacc[vacc['location']== state][['date','total_vaccinations']][-7:]
    new_vacc['total_vaccinations in Millions']= new_vacc['total_vaccinations']//1000
    new_vacc['percentage'] = new_vacc['total_vaccinations'] / state_doses[state] * 100
    source = ColumnDataSource(new_vacc)
    
    dates = source.data['date'].tolist()
    p = figure(x_range=dates, title= f'Total Vaccinations in {state} (last 7 days recorded)')
    p.line(x='date', y='total_vaccinations in Millions', source=source, legend_label="Number of Vaccinations", line_width=8,line_color="green")
    p.add_tools(HoverTool())
    p.yaxis.axis_label = 'Total Number of Vaccinations (Millions)'
    p.xaxis.axis_label = 'Date (Day.Month.Year)'
    p.legend.location = "top_left"
    return p

def line_chart_2(state):
    total = read_total()
    vacc = read_vacc()
    state_doses   = dict(zip(total.location,total.doses_needed))
    new_vacc = vacc[vacc['location']== state][['date','total_vaccinations']][-7:]
    new_vacc['total_vaccinations in Millions']= new_vacc['total_vaccinations']//1000
    new_vacc['percentage'] = new_vacc['total_vaccinations'] / state_doses[state] * 100
    source = ColumnDataSource(new_vacc)
    dates = source.data['date'].tolist()
    p = figure(x_range=dates, title= f'Percentage of People Fully Vaccinated in {state} for last 7 days recorded')
    p.line(x='date', y='percentage', source=source, legend_label="Number of Vaccinations", line_width=8,line_color="green")
    p.add_tools(HoverTool())
    p.yaxis.axis_label = 'Percentage of People Fully Vaccinated (%)'
    p.xaxis.axis_label = 'Date (Day.Month.Year)'
    p.legend.location = "top_left"

    return p

line_chart_2(state)

if (__name__ == "__main__"):
    line_chart_1(state= 'Alabama')
    line_chart_2(state='Alabama')



