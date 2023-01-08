SRC is shared among exceutor and submit host
exceutor using python 3.8 where subbmit hose use virtual env 3.9(in src\env)

src\runs is a folder to store all dagman workflow history, which are
1. CSV Prediction
2. AUTO train and test and update model 
The workflow function can be found on 
src\dag.py and src\dag2.py



JUST ignore old testing code(src\archieve)


src\api_fuction.py
src\app.py
both file is to host the API


go into src\shared
src\shared\temp store the CSV file when user call API to upload
src\shared\data_received IGNORE this folder
src\shared\model store 2 random forest , one is updated the best model, one is baseline model(why? I scare when something went wrong with the best model, and we still can use baseline model)
src\shared\script contains all the script to support dagman workflow
src\shared\script\config.py IGNORE this file
src\shared\script\raw.csv.py IGNORE this file
src\shared\script\raw_100.csv.py IGNORE this file

please read src\dag.py and src\dag2.py, and the src\runs to see how the dagman and htcondor work
