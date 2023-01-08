#!/usr/bin/env python3
import pandas as pd
import numpy as np
import sys, os
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

args = sys.argv[1].split(";")
print(args)

input_path = args[0]
setting=args[1]

# input_path = "/home/ubuntu"
# setting="1"
full_path = os.path.join(input_path,"training.csv")
print(full_path)

train = pd.read_csv(full_path)

X_train = train.drop('bonus', axis=1)
y_train = train['bonus']

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X1_train = sc.fit_transform(X_train)

if setting=="1":
    regressor = RandomForestRegressor(bootstrap = False, 
                                  max_depth = 100,
                                  max_features = 'sqrt',
                                  min_samples_leaf = 1,
                                  min_samples_split = 2,
                                  n_estimators = 88).fit(X1_train, y_train)
elif setting=="2":
    regressor = RandomForestRegressor(#criterion = 'gini', 
                                  max_depth = 2,
                                  max_features = 'log2',
                                  min_samples_leaf = 1,
                                  min_samples_split = 2,
                                  n_estimators = 88).fit(X1_train, y_train)
elif setting=="3":
    regressor = RandomForestRegressor(bootstrap = True, 
                                  max_depth = None,
                                  max_features = 'auto',
                                  min_samples_leaf = 1,
                                  min_samples_split = 2,
                                  n_estimators = 100,
                                  verbose = 0).fit(X1_train, y_train)
                                  
#save the model
import pickle
filename = 'model_{}.sav'.format(setting)
pickle.dump(regressor, open(filename, 'wb'))



# y1_pred = regressor.predict(X1_test)
# print('Mean Absolute Error:', mean_absolute_error(y1_test, y1_pred).round(2))
# print('Root Mean Squared Error:', np.sqrt(mean_squared_error(y1_test, y1_pred)).round(2))
# print("Mean squared error (linear model): {:.2f}".format(mean_squared_error(y1_test, y1_pred)))
# print("r2_score (linear model): {:.2f}".format(r2_score(y1_test, y1_pred)))