# import pandas as pd
# import sqlite3 as sql
# # from bokeh.io import push_notebook, output_notebook 
# from bokeh.plotting import figure,show
# from bokeh.embed import components
# from bokeh.models import ColumnDataSource, HoverTool,Legend
# # from bokeh.palettes import Magma,RdYlGn
# # from bokeh.transform import factor_cmap



# def line_chart_1(state):
#     new_vacc = vacc[vacc['location']== state][['date','total_vaccinations']][-7:]
#     new_vacc['total_vaccinations in Millions']= new_vacc['total_vaccinations']//1000
#     new_vacc['percentage'] = new_vacc['total_vaccinations'] / state_doses[state] * 100
#     source = ColumnDataSource(new_vacc)
    
#     dates = source.data['date'].tolist()
#     p = figure(x_range=dates, title= f'Total Vaccinations in {state} (last 7 days recorded)')
#     p.line(x='date', y='total_vaccinations in Millions', source=source, legend_label="Number of Vaccinations", line_width=8,line_color="green")
#     p.add_tools(HoverTool())
#     p.yaxis.axis_label = 'Total Number of Vaccinations (Millions)'
#     p.xaxis.axis_label = 'Date (Day.Month.Year)'
#     p.legend.location = "top_left"

#     show(p)
#     return p

# line_chart_1(state)

