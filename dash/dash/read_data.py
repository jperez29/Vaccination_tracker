import pandas as pd
import sqlite3 as sql
import functools

@functools.lru_cache(maxsize=None)
def create_connect(db='project_2.db'):
    conn = sql.connect(db)
    return conn

@functools.lru_cache(maxsize=None)
def read_vacc():
    conn = create_connect(db='project_2.db')
    df = pd.read_sql("SELECT * from vacc", conn, index_col='index')
    return df

@functools.lru_cache(maxsize=None)
def read_total():
    conn = create_connect(db='project_2.db')
    df = pd.read_sql("SELECT * from total", conn, index_col='index')
    return df

if (__name__ == "__main__"):
    create_connect(db='project_2.db')
    read_vacc()
    read_total()