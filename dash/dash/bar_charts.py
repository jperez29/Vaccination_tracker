import pandas as pd
import sqlite3 as sql
import functools
from bokeh.plotting import figure,show
# from bokeh.embed import components
from bokeh.models import ColumnDataSource, HoverTool,Legend
from bokeh.palettes import Magma,RdYlGn,Greens
from bokeh.transform import factor_cmap
from .read_data import create_connect,read_vacc, read_total
from bokeh.io import curdoc

@functools.lru_cache(maxsize=None)
def top_states():
    options = [1,2,3,4,5,6,7,8,9]
    selection= options[4]
    total = read_total()  
    total = total.sort_values('perc_daily_vacc_pop',ascending=False)
    top_total = total[:selection]
    source = ColumnDataSource(top_total)
    country_names = source.data['location'].tolist()
    colors = factor_cmap('location', palette=Greens[selection], factors=country_names)
    p = figure(y_range=country_names, title= f'The {selection} States with Highest Pop Fully Vaccinated (%) in Ascending Order')
    p.hbar(y='location', right='perc_daily_vacc_pop', source=source, height=0.8, color=colors)
    p.add_tools(HoverTool())
    curdoc().theme = 'dark_minimal'
    p.xaxis.axis_label = 'Total Population Vaccinated (%)'
    p.yaxis.axis_label = 'State'
    return p

top_states()

@functools.lru_cache(maxsize=None)
def bottom_states():
    options = [1,2,3,4,5,6,7,8,9]
    selection= options[4]
    total = read_total()  
    bottom_total = total[-selection:].sort_values('perc_daily_vacc_pop',ascending=True)
    source = ColumnDataSource(bottom_total)
    country_names = source.data['location'].tolist()
    colors = factor_cmap('location', palette=Magma[selection], factors=country_names)
    p = figure(y_range=country_names, title= f'The {selection} States with Lowest Pop Fully Vaccinated (%) in Descending Order')
    p.hbar(y='location', right='perc_daily_vacc_pop', source=source, height=0.8, color=colors)
    p.add_tools(HoverTool())
    p.xaxis.axis_label = 'Total Population Vaccinated (%)'
    p.yaxis.axis_label = 'State'
    return p

bottom_states()

if (__name__ == "__main__"):
    top_states()
    bottom_states()