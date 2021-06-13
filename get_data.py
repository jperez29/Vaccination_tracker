import pandas as pd
import numpy as np
import datetime
import kaggle
from sqlalchemy import create_engine

engine = create_engine('sqlite:///dash/project_2.db', echo=False)

links = ["berkayalan/vaccinations-in-united-states"]
def get_vac_data(): # Split this into get_stroke_data and parse_stroke_data
    api = kaggle.KaggleApi()
    api.authenticate()
    for link in links:
        api.dataset_download_files(link, unzip=True, quiet=False)
    vacc = pd.read_csv("us_vaccinations.csv")
    
    start = datetime.datetime.now()
    while True:
        if datetime.datetime.now() > (start +  datetime.timedelta(seconds=1)):
            api.authenticate()
            for link in links:
                api.dataset_download_files(link, unzip=True, quiet=False)
            vacc = pd.read_csv("us_vaccinations.csv")

        yield vacc

def creating_db():  
    dataframes = get_vac_data()
    vacc = next(dataframes)
    print(vacc)
    moving_vac_to_db = vacc.to_sql('vacc', con=engine, if_exists='append')

def check_db(table_name):
    df= pd.read_sql_table(table_name, con=engine)
    while True:
        yield df

if (__name__ == "__main__"):
     creating_db()
     check_db(table_name="vacc")