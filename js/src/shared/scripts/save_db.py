#!/usr/bin/env python3
import pandas as pd
import os
from sqlalchemy import create_engine
db_server= 'database-gs.czef6uqdcxjz.us-east-1.rds.amazonaws.com,1433'
db_name="parallel"
db_port = "1433"
db_user= "admin"
db_pwd="parallelcomputing2022"
connection_string_sql_alchemy = 'mssql+pyodbc://{}:{}@{}:{}/{}?driver=ODBC+Driver+17+for+SQL+Server'.format(db_user\
                                    ,db_pwd, db_server,db_port, db_name)
                                    
def append_data(df):
    engine = create_engine(connection_string_sql_alchemy)
    df.set_index(df.columns[0],inplace=True)
    print(df)
    df.to_sql('data',con = engine,if_exists = 'append')
    print("done")
    
import sys
args = sys.argv[1].split(";")
input_path = args[0]
full_path = os.path.join(input_path,"predicted.csv")
df = pd.read_csv(full_path)
append_data(df)