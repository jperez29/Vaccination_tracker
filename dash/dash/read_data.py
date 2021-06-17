import pandas as pd
import sqlite3 as sql

def read_vacc():
    db = 'project_2.db'
    conn = sql.connect(db)
    df = pd.read_sql("SELECT * from vacc", conn, index_col='index')
    return df

def read_total():
    db = 'project_2.db'
    conn = sql.connect(db)
    df = pd.read_sql("SELECT * from total", conn, index_col='index')
    return df

if (__name__ == "__main__"):
    read_df()