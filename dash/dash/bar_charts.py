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

# @functools.lru_cache(maxsize=None)
def bottom_states():
    selection= 5
    total = read_total()  
    top_total = total[:selection].sort_values('perc_daily_vacc_pop',ascending=False)
    source = ColumnDataSource(top_total)
    country_names = source.data['location'].tolist()
    colors = factor_cmap('location', palette=Greens[selection], factors=country_names)
    p = figure(y_range=country_names, title= f'The {selection} States with Lowest Pop Fully Vaccinated (%)')
    p.hbar(y='location', right='perc_daily_vacc_pop', source=source, height=0.8, color=colors)
    p.add_tools(HoverTool())
    p.xaxis.axis_label = 'Total Population Vaccinated (%)'
    p.yaxis.axis_label = 'State'

    return p


# @functools.lru_cache(maxsize=None)
def top_states():
    selection= 5
    total = read_total()  
    bottom_total = total[-selection:].sort_values('perc_daily_vacc_pop',ascending=True)
    source = ColumnDataSource(bottom_total)
    country_names = source.data['location'].tolist()
    colors = factor_cmap('location', palette=Magma[selection], factors=country_names)
    p = figure(y_range=country_names, title= f'The {selection} States with Highest Pop Fully Vaccinated (%)')
    p.hbar(y='location', right='perc_daily_vacc_pop', source=source, height=0.8, color=colors)
    p.add_tools(HoverTool())
    p.xaxis.axis_label = 'Total Population Vaccinated (%)'
    p.yaxis.axis_label = 'State'

    return p


if (__name__ == "__main__"):
    top_states()
    bottom_states()