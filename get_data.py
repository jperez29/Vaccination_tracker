import pandas as pd
import datetime
import kaggle
from sqlalchemy import create_engine

engine = create_engine('sqlite:///dash/project_2.db', echo=False)

links = ["berkayalan/vaccinations-in-united-states"]
def get_vac_data(): 
    api = kaggle.KaggleApi()
    api.authenticate()
    for link in links:
        api.dataset_download_files(link, unzip=True, quiet=False)
    vacc = pd.read_csv("us_state_vaccinations.csv", sep=';')
    return vacc

def creating_db():  
    vacc = get_vac_data()
    moving_vac_to_db = vacc.to_sql('vacc', con=engine, if_exists='append')

def check_db(table_name):
    df= pd.read_sql_table(table_name, con=engine)
    while True:
        yield df

if (__name__ == "__main__"):
     creating_db()
     check_db(table_name="vacc")