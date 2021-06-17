import pandas as pd
import requests
from bs4 import BeautifulSoup
import sqlite3 as sql

url1 = 'https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population'
url = 'https://developers.google.com/public-data/docs/canonical/states_csv'

def state_pop(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    rows = soup.find_all('tr')
    th_td_list = []
    for row in rows[2:54]:
        tds = row.findAll('td')
        th_td_data_row = []
        for td in tds[2:]:
            td_text = td.text.strip()
            td_text = td_text.replace(',',"")              
            th_td_data_row.append(td_text)              
        th_td_list.append(th_td_data_row[:2])
    return th_td_list

def state_coor(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    rows = soup.find_all('tr')
    th_td_list = []
    for row in rows:
        tds = row.findAll('td')
        th_td_data_row = []
        for td in tds:
            td_text = td.text.strip()
            td_text = td_text.replace(',',"")              
            th_td_data_row.append(td_text)              
        th_td_list.append(th_td_data_row)
    return th_td_list

def pop_table():
    coor = pd.DataFrame(state_coor(url)[1:], columns= ['state', 'latitude', 'longitude','location'])
    coor = coor.replace("New York", "New York State")

    pop = pd.DataFrame(state_pop(url1), columns= ['location','state_population'])
    pop = pop.replace("New York", "New York State")
    pop['state_population'] = pop['state_population'].astype('int64')

    totals = pd.merge(coor, pop, on="location")
    return totals

if (__name__ == "__main__"):
    pop_table()
