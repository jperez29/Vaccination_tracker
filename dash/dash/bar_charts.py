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
def top_states():
    curdoc().clear()
    options = [1,2,3,4,5,6,7,8,9]
    selection= options[4]
    total = read_total()  
    total = total.sort_values('perc_daily_vacc_pop',ascending=False)
    top_total = total[:selection]
    source_1 = ColumnDataSource(top_total)
    country_names = source_1.data['location'].tolist()
    colors = factor_cmap('location', palette=Greens[selection], factors=country_names)
    p_bar = figure(y_range=country_names, title= f'The {selection} States with Highest Pop Fully Vaccinated (%) in Ascending Order')
    p_bar.hbar(y='location', right='perc_daily_vacc_pop', source=source_1, height=0.8, color=colors)
    hover3 = HoverTool()
    p_bar.add_tools(hover3)
    p_bar.xaxis.axis_label = 'Total Population Vaccinated (%)'
    p_bar.yaxis.axis_label = 'State'
    return p_bar


# @functools.lru_cache(maxsize=None)
def bottom_states():
    curdoc().clear()
    options = [1,2,3,4,5,6,7,8,9]
    selection= options[4]
    total = read_total()  
    bottom_total = total[-selection:].sort_values('perc_daily_vacc_pop',ascending=True)
    source_2 = ColumnDataSource(bottom_total)
    country_names = source_2.data['location'].tolist()
    colors = factor_cmap('location', palette=Magma[selection], factors=country_names)
    p_bar_two = figure(y_range=country_names, title= f'The {selection} States with Lowest Pop Fully Vaccinated (%) in Descending Order')
    p_bar_two.hbar(y='location', right='perc_daily_vacc_pop', source=source_2, height=0.8, color=colors)
    hover4 = HoverTool()
    p_bar_two.add_tools(hover4)
    p_bar_two.xaxis.axis_label = 'Total Population Vaccinated (%)'
    p_bar_two.yaxis.axis_label = 'State'
    return p_bar_two


if (__name__ == "__main__"):
    top_states()
    bottom_states()