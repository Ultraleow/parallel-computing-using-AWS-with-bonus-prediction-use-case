#!/usr/bin/env python3
import json
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import os, pickle
import sys
new_model = r"/home/ubuntu/src/shared/model/rf_model_best.sav"
sure_model = r"/home/ubuntu/src/shared/model/rf_model.sav"


def csv_predict(df):
    try:
        loaded_model = pickle.load(open(new_model, 'rb'))
    except:
        loaded_model = pickle.load(open(sure_model, 'rb'))
        print("using old model")
    y = loaded_model.predict(df)
    return y

#csv_path = "/home/ubuntu/src/shared/scripts/raw.csv"
args = sys.argv[1].split(";")
path = args[0]
input_path = args[0]


csv_path = input_path+"/pprocessed.csv"
df = pd.read_csv(csv_path)
result = csv_predict(df)
print(result)
df["bonus"] = result
df.to_csv("predicted.csv", index=False)


csv_path = input_path+"/raw.csv"
df = pd.read_csv(csv_path)
df["bonus"] = result
df.to_csv("predicted_email.csv", index=False)


    
    