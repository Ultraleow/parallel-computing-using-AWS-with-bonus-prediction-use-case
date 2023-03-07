#!/usr/bin/env python3
import pandas as pd
import numpy as np
import pickle
import sys, os
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error



args = sys.argv[1].split(";")
print(args)
input_path = args[0]
setting=args[1]

# input_path = "/home/ubuntu"
# setting="1"
full_path = os.path.join(input_path,"testing.csv")
model = os.path.join(input_path,"model_{}.sav".format(setting))
test = pd.read_csv(full_path)
print(full_path)

X_test = test.drop('bonus', axis=1)
y1_test = test['bonus']

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X1_test = sc.fit_transform(X_test)


loaded_model = pickle.load(open(model, 'rb'))
y1_pred = loaded_model.predict(X1_test)
r2 = r2_score(y1_test, y1_pred)
print('Mean Absolute Error:', mean_absolute_error(y1_test, y1_pred).round(2))
print('Root Mean Squared Error:', np.sqrt(mean_squared_error(y1_test, y1_pred)).round(2))
print("Mean squared error (linear model): {:.2f}".format(mean_squared_error(y1_test, y1_pred)))
print("r2_score (linear model): {:.2f}".format(r2))
np.save("r2_{}.npy".format(setting),r2)
