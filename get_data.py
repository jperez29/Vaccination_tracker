import pandas as pd
import datetime
import kaggle

links = ["berkayalan/vaccinations-in-united-states"]
def get_vac_data(): 
    api = kaggle.KaggleApi()
    api.authenticate()
    for link in links:
        api.dataset_download_files(link, unzip=True, quiet=False)
    vacc = pd.read_csv("us_state_vaccinations.csv", sep=';')
    return vacc

if (__name__ == "__main__"):
     get_vac_data()
