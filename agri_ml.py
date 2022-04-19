import numpy as np
import pandas as pd
import sklearn
import pickle
data = pd.read_csv('data.csv')
data.head()
# print(data.head())
from sklearn.model_selection import train_test_split
x1= data.drop(['label'],axis=1)
y1 = data['label']
x1_train,x1_test,y1_train,y1_test = train_test_split(x1,y1, test_size=0.2, random_state=0)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, confusion_matrix, classification_report
lr = LogisticRegression()
lr.fit(x1_train,y1_train)
# lr.score(x_test,y_test)
y_pred = lr.predict(x1_test)
# print(classification_report(y1_test,y_pred))
# print(lr.predict([[69,37,42,23.05804872,83.37011772,7.073453503,251.0549998]]
# ))

pickle.dump(lr, open('model.pkl','wb'))