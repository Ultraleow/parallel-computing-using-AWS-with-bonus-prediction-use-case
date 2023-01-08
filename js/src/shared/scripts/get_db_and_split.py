#!/usr/bin/env python3
import pandas as pd
from sqlalchemy import create_engine
db_server= 'database-gs.czef6uqdcxjz.us-east-1.rds.amazonaws.com,1433'
db_name="parallel"
db_port = "1433"
db_user= "admin"
db_pwd="parallelcomputing2022"
connection_string_sql_alchemy = 'mssql+pyodbc://{}:{}@{}:{}/{}?driver=ODBC+Driver+17+for+SQL+Server'.format(db_user\
                                    ,db_pwd, db_server,db_port, db_name)

def get_all_data():
    engine = create_engine(connection_string_sql_alchemy)
    df = pd.read_sql(
        'SELECT * FROM [data] where  [bonus] is not NULL',
        engine)
    return df
df = get_all_data()

df=df.sample(frac=1)
training = df.sample(frac = 0.8)
testing = df.drop(training.index)
training.to_csv("training.csv", index=False)
testing.to_csv("testing.csv", index=False)