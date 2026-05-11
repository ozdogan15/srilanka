# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics

# read the data
df = pd.read_excel('maha_rice_yield_vars_district_1999_2022.xlsx')
df = df.dropna()


X = df[['year','GCImax','rainy_days','VPD','rain','dry_spells','temp_gt30_days']]
Y = df['yield']
#print(X)
#print(Y)

X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.25)

# create regressor object
model = RandomForestRegressor(n_estimators = 150)

model.fit(X_train, y_train) 

y_pred = model.predict(X_test)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

plt.plot(y_test,y_pred,'o',color='black')
plt.xlim(0, 7000)
plt.ylim(0, 7000)
plt.show()



