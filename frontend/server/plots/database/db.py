# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, text
import matplotlib.pyplot as plt
import pandas as pd

engine = create_engine('postgresql://postgres:root2010@postgres.cfj83pcaofse.us-east-1.rds.amazonaws.com/postgres')
conn = engine.connect()

def runQuery(sql):
    result = conn.execution_options(isolation_level="AUTOCOMMIT").execute((text(sql)))
    return pd.DataFrame(result.fetchall(), columns=result.keys())

def save_replace(df, table_name):
    df.to_sql(name=table_name, con=conn, if_exists="replace", method="multi")