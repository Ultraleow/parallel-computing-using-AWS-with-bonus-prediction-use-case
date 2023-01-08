#!/usr/bin/env python3
import pandas as pd
import numpy as np
import shutil
import os
import sys
from sqlalchemy import create_engine
db_server= 'database-gs.czef6uqdcxjz.us-east-1.rds.amazonaws.com,1433'
db_name="parallel"
db_port = "1433"
db_user= "admin"
db_pwd="parallelcomputing2022"


args = sys.argv[1].split(";")
input_path = args[0]

#input_path = "/home/ubuntu"

model_1 = os.path.join(input_path,"model_{}.sav".format(1))
model_2 = os.path.join(input_path,"model_{}.sav".format(2))
model_3 = os.path.join(input_path,"model_{}.sav".format(3))

result_1 = os.path.join(input_path,"r2_{}.npy".format(1))
result_2 = os.path.join(input_path,"r2_{}.npy".format(2))
result_3 = os.path.join(input_path,"r2_{}.npy".format(3))

connection_string_sql_alchemy = 'mssql+pyodbc://{}:{}@{}:{}/{}?driver=ODBC+Driver+17+for+SQL+Server'.format(db_user\
                                    ,db_pwd, db_server,db_port, db_name)
def get_r2():
    engine = create_engine(connection_string_sql_alchemy)
    df = pd.read_sql(
        'SELECT [r2] FROM [metri]',
        engine)
    return df["r2"][0]
    
db_r2 = get_r2()
print(type(db_r2))
def move_and_replace(model):
    shutil.move(model,'/home/ubuntu/src/shared/model/rf_model_best.sav')
def compare_and_update(result,model):
    if np.load(result)>db_r2:
        move_and_replace(model)
        
        

compare_and_update(result_1,model_1)
compare_and_update(result_2,model_2)
compare_and_update(result_3,model_3)