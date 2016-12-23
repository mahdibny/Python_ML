# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 01:40:23 2016
sentdex tutorial on youtube

Regression: Best Fit Line of Data
y=mx+b

Supervised Learning
-Features
    in this data set
    -Open, High, Low ...
    -Adj.Close

-Labes
    -Price of stock

@author: Mahdi
"""

import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

#create dataframe then keep only important data
df=quandl.get('WIKI/GOOGL')
df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]] 

#adding two new cols HLPCT, PCTchange
df['HL_PCT']=(df['Adj. High']-df['Adj. Close'])/df['Adj. Close'] *100
df['PCT_change']=(df['Adj. Close']-df['Adj. Open'])/df['Adj. Open'] *100
df=df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

#creating a varible and making outliers of missing data
forecast_col='Adj. Close'
df.fillna(-99999, inplace=True)

#number of days out - 10% out
forecast_out=int(math.ceil(0.01*len(df))) #rounds to nearest whole integer
# 32 days in advance

#creating label colm
#shifting by integer
df['label']=df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

#defining x and y 
X = np.array(df.drop(['label'],1)) #features
Y = np.array(df['label'])        #label
X = preprocessing.scale(X) #scaling the x value

X_train,X_test,Y_train,Y_test=cross_validation.train_test_split(X,Y,test_size=0.2)
#20% data

#classifer
clf=LinearRegression()
#cls=LinearRegression(n_jobs=2) #parallel process
#clf=svm.SVR()
#clf=svm.SVR(kernel='poly')
clf.fit(X_train,Y_train)
clf.score(X_test,Y_test)
accuracy=clf.score(X_test,Y_test) #squared error 
print(accuracy)

#we want to use svm regression not simple linear regerssion
#line 59 commented in 58 commentd out
#results show svm is .804 and Linear Regression() .9685
#polynomial kernal gave us .6597

#Linear Regression njobs 