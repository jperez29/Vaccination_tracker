from get_data import get_vac_data
import pandas as pd
import sqlite3 as sql
import math

# create_table = creating_db()

# db = 'dash/project_2.db'
# conn = sql.connect(db)


def fill_empty(col, df):
    last_update = 0
    lst = []
    for row in df[col]:
        if math.isnan(row):
            row = last_update
        else:
            last_update = row
        lst.append(row)
    df[col] = lst


# def read_df():
#     df = pd.read_sql("SELECT * from vacc", conn, index_col='index')
#     return df


def clean_data(dataframe_name):
    df = dataframe_name
    no_states = ['Bureau of Prisons', 'Dept of Defense', 'Federated States of Micronesia', 'Indian Health Svc', 'Long Term Care','Marshall Islands', 'Republic of Palau', 'Veterans Health', 'United States']
    df = df[~df['location'].isin(no_states)]
    modified = ['total_vaccinations', 'total_distributed', 'people_vaccinated', 'people_fully_vaccinated_per_hundred',
       'total_vaccinations_per_hundred', 'people_fully_vaccinated',
       'people_vaccinated_per_hundred', 'distributed_per_hundred',
       'share_doses_used']
    for column in modified:
        fill_empty(column, df=df)
    df= df.fillna(0)
    # df.to_sql("vacc", conn, if_exists="replace")
    return df

if (__name__ == "__main__"):
    creating_db()
    clean_data()