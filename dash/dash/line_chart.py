import pandas as pd
import sqlite3 as sql
from bokeh.plotting import figure,show
from bokeh.embed import components
from bokeh.models import ColumnDataSource, HoverTool,Legend
from bokeh.transform import factor_cmap
from .read_data import create_connect,read_vacc, read_total
from bokeh.palettes import Magma,RdYlGn


state = 'Alabama'
def line_chart_1(state):
    total = read_total()
    vacc = read_vacc()
    state_doses   = dict(zip(total.location,total.doses_needed))
   
    new_vacc = vacc[vacc['location']== state][['date','total_vaccinations']][-7:]
    new_vacc['total_vaccinations in Millions']= new_vacc['total_vaccinations']//1000
    new_vacc['percentage'] = new_vacc['total_vaccinations'] / state_doses[state] * 100
    source_3 = ColumnDataSource(new_vacc)
    
    dates = source_3.data['date'].tolist()
    p_line = figure(x_range=dates, title= f'Total Vaccinations in {state} (last 7 days recorded)')
    p_line.line(x='date', y='total_vaccinations in Millions', source=source_3, legend_label="Number of Vaccinations", line_width=8,line_color="green")
    hover1 = HoverTool()
    p_line.add_tools(hover1)
    p_line.yaxis.axis_label = 'Total Number of Vaccinations (Thousand)'
    p_line.xaxis.axis_label = 'Date (Day.Month.Year)'
    p_line.legend.location = "top_left"
    return p_line

def line_chart_2(state):
    total = read_total()
    vacc = read_vacc()
    state_doses   = dict(zip(total.location,total.doses_needed))
    new_vacc = vacc[vacc['location']== state][['date','total_vaccinations']][-7:]
    new_vacc['total_vaccinations in Millions']= new_vacc['total_vaccinations']//1000
    new_vacc['percentage'] = new_vacc['total_vaccinations'] / state_doses[state] * 100
    source_4 = ColumnDataSource(new_vacc)
    dates = source_4.data['date'].tolist()
    p_line_two = figure(x_range=dates, title= f'Percentage of People Fully Vaccinated in {state} for last 7 days recorded')
    p_line_two.line(x='date', y='percentage', source=source_4, legend_label="Number of Vaccinations", line_width=8,line_color="green")
    hover2 = HoverTool()
    p_line_two.add_tools(hover2)
    p_line_two.yaxis.axis_label = 'Percentage of People Fully Vaccinated (%)'
    p_line_two.xaxis.axis_label = 'Date (Day.Month.Year)'
    p_line_two.legend.location = "top_left"

    return p_line_two

def scatter_plot():
    total = read_total()
    total = total.sort_values(by='doses_needed', ascending=False)
    total['total_vaccinations_thousand']= total['doses_needed']//1000
    doses = total['total_vaccinations_thousand'].values
    percentage = total['perc_daily_vacc_pop'].values

    colors = [x for x in Magma[4]]*13

    p = figure(title = "State Percentage and Doses distribution")
    p.xaxis.axis_label = 'Percentage of People Fully Vaccinated (%)'
    p.yaxis.axis_label = 'total Doses Needed (thousand)'

    p.circle(percentage, doses,color=colors, fill_alpha=0.4, size=10)

    hover = HoverTool()
    p.add_tools(hover)

    return p


if (__name__ == "__main__"):
    line_chart_1(state= 'Alabama')
    line_chart_2(state='Alabama')
    scatter_plot()



