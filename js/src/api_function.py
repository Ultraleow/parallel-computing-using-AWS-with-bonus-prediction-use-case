import json
import pandas as pd
import threading, os
from flask import Blueprint, Response, request
from dag import csv_prediction_workflow
from dag2 import auto_train_workflow
import utils
from preprocess import convert_all_value
from datetime import datetime, timedelta
from utils import append_data
    

app_func = Blueprint('app_func', __name__)

@app_func.route('/health_check_2')
def checking():  # put application's code here
    return 'Hello heallty 2'


def predict_workflow(file,email_to,api=True):
        csv_prediction_workflow(file,email_to)
def auto_training():
        auto_train_workflow()
        
@app_func.route('/upload_csv', methods=['POST'])
def predict_csv_and_email():  # put application's code here
    
    
    file_uploaded = request.files["csv_file"]
    user_email= request.form["email"]
    print(file_uploaded)
    print(user_email)
    df = pd.read_csv(file_uploaded)
    now = datetime.now() + timedelta(hours=8)
    dt_string = now.strftime("%H%M%S_%f_%Y%m%d")
    export_path = os.path.join("/home/ubuntu//src/shared/temp","file_{}.csv".format(dt_string))
    df.to_csv(export_path, index=False)
    no_row =len(df)
    
    print(no_row)
    thread = threading.Thread(target=predict_workflow, kwargs={'file': export_path,'email_to':user_email})
    thread.start()
    if no_row>=50:
        thread = threading.Thread(target=auto_training)
        thread.start()
    return "Wait for Email"


def save_data(dataframe):
        # do something that takes a long time
        print("RUN")
        append_data(dataframe)

@app_func.route('/predict', methods=['POST'])
def inference():  # put application's code here
    df = convert_all_value(pd.DataFrame([request.form.to_dict()]))
    print(df)
    result = int(utils.inference(df))
    df["bonus"] = result
    thread = threading.Thread(target=save_data, kwargs={'dataframe': df})
    thread.start()

    return json.dumps(result)
