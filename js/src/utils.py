from sklearn.ensemble import RandomForestRegressor
import os, pickle
import pandas as pd
from sqlalchemy import create_engine
db_server= 'database-gs.czef6uqdcxjz.us-east-1.rds.amazonaws.com,1433'
db_name="parallel"
db_port = "1433"
db_user= "admin"
db_pwd="parallelcomputing2022"
connection_string_sql_alchemy = 'mssql+pyodbc://{}:{}@{}:{}/{}?driver=ODBC+Driver+17+for+SQL+Server'.format(db_user\
                                    ,db_pwd, db_server,db_port, db_name)

new_model = "/home/ubuntu/src/shared/model/rf_model_best.sav"
sure_model = "/home/ubuntu/src/shared/model/rf_model.sav"


def inference(single_data):
    try:
        loaded_model = pickle.load(open(new_model, 'rb'))
    except:
        loaded_model = pickle.load(open(sure_model, 'rb'))
        print("using old model")
    y = loaded_model.predict(single_data)
    return y

def append_data(df):
    print("running")
    engine = create_engine(connection_string_sql_alchemy)
    df.set_index(df.columns[0],inplace=True)
    print(df)
    df.to_sql('data',con = engine,if_exists = 'append')
    print("done")