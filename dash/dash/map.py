import pandas as pd
import sqlite3 as sql
import functools
from bokeh.io import push_notebook, output_notebook 
from bokeh.plotting import figure,show
from bokeh.embed import components
from bokeh.models import ColumnDataSource, Legend
from bokeh.palettes import YlGnBu9 as YlGnBu
from bokeh.models import LogColorMapper
from bokeh.sampledata.us_states import data as us_states
from bokeh.models import LinearColorMapper
from bokeh.models import ColorBar
from .read_data import create_connect,read_vacc, read_total
from bokeh.io import curdoc


# @functools.lru_cache(maxsize=None)
def state_map(): 
    curdoc().clear() 
    total = read_total()
    us_states_df = pd.DataFrame(us_states).T
    us_states_df = us_states_df.rename(columns={"name": "location"})
    us_states_df = us_states_df.replace("New York", "New York State")
    us_states_df = us_states_df[~us_states_df["location"].isin(['Alaska', "Hawaii"])]
    us_states_df["lons"] = us_states_df.lons.values.tolist()
    us_states_df["lats"] = us_states_df.lats.values.tolist()
    us_states_df = pd.merge(total, us_states_df, on="location")
    
    us_states_datasource = {}
    us_states_datasource["lons"] = us_states_df.lons.values.tolist()
    us_states_datasource["lats"] = us_states_df.lats.values.tolist()
    us_states_datasource["location"] = us_states_df.location.values.tolist()
    us_states_datasource["StateCodes"] = us_states_df.state.values.tolist()
    us_states_datasource["PercVacc"] = us_states_df.perc_daily_vacc_pop.values.tolist()
    
    fig = figure(plot_width=1200, plot_height=700,
                 title="United States Percentage of total Vaccinations Per State Choropleth Map",
                 x_axis_location=None, y_axis_location=None,
                 tooltips=[
                            ("Location", "@location"), ("PercentageVaccinations", "@PercVacc"), ("(Long, Lat)", "($x, $y)")
                          ])
    palette =YlGnBu[::-1]
    color_mapper = LinearColorMapper(palette, low=0, high =70)
    color_bar = ColorBar(color_mapper=color_mapper)
    fig.grid.grid_line_color = None
    fig.patches("lons", "lats", source=us_states_datasource,
                fill_color={'field': 'PercVacc', 'transform': color_mapper},
                fill_alpha=0.7, line_color="white", line_width=0.5)
    fig.add_layout(color_bar,'left')

    return fig

if (__name__ == "__main__"):
    state_map()