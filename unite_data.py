import pandas as pd
import datetime
import kaggle
import math
from sqlalchemy import create_engine
from get_data import get_vac_data
from clean_data import fill_empty, clean_data
from pop_data import state_pop, state_coor, pop_table
 
engine = create_engine('sqlite:///dash/project_2.db', echo=False)
links = ["berkayalan/vaccinations-in-united-states"]

def clean_vacc():  
    vacc = get_vac_data()
    vacc = clean_data(vacc)
    return vacc

def final_totals():
    df = clean_vacc()
    tot_vacc = df.groupby('location')[['location', 'daily_vaccinations']].sum()
    tot_vacc['daily_vaccinations'] = tot_vacc['daily_vaccinations'].astype(int)
    totals = pop_table()
    final = pd.merge(totals, tot_vacc, on="location")
    final['doses_needed'] = final['state_population'] * 2
    final['perc_daily_vacc_pop'] = final['daily_vaccinations'] / final['doses_needed'] * 100
    final['perc_daily_vacc_pop'] = final['perc_daily_vacc_pop'].astype(int)
    return final

def creating_db():
    totals_table = final_totals()
    vacc_table = clean_vacc()
    moving_vac_to_db = vacc_table.to_sql('vacc', con=engine, if_exists='append')
    moving_totals_to_db = totals_table.to_sql('total', con=engine, if_exists='append')

if (__name__ == "__main__"):
    final_totals()
    creating_db()

