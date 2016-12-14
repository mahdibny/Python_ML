# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:46:31 2016

Learning Pandas Chapter 5

@author: Mahdi
"""
from pandas import Series,DataFrame
import pandas as pd

#two important datastructures
#Series
#DataFrame

""""
Series Intro
"""""

#Lets start with Series
#one dimensional array like object
#also has index
obj=Series([4,7,-5,3])
"""
obj
Out[55]: 
0    4
1    7
2   -5
3    3
"""
obj.values #returns values
obj.index  #returns index

obj2=Series([4,7,-5,3],index=['d','b','a','c'])
#now we change the idex of the series

'''''''''''''''
'''''''''''''''

#if we want we can preform operations on the 
#data and the indices will remain
objtemp2=obj2*2
#it can be thought of as an ordered dict

#if one has an data in a python dict then they
#can create a Series from it
sdata={'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
obj3=Series(sdata)
# the index will be the dict keys
"""
obj3
Out[59]: 
Ohio      35000
Oregon    16000
Texas     71000
Utah       5000
dtype: int64
"""

'''''''''''''''
'''''''''''''''

states=['California','Ohio','Oregon','Texas']
obj4=Series(sdata,index=states)
#here we pass in new index will bind the previous
#data for each state but for california be NaN
"""
obj4
Out[61]: 
California        NaN
Ohio          35000.0
Oregon        16000.0
Texas         71000.0
dtype: float64
"""

pd.isnull(obj4)
#returns that which is null value as true
pd.notnull(obj4)

#one can also add differently index series with +
obj5=obj3+obj4
#it will add the values of each index


#the values and index can be assigned names 
obj4.name='population'
obj4.index.name='state'


#a series index can also be changed
obj.index=['Bob','Steve','Jeff','Ryan']


"""
Data Frame
"""

#tabular, spreadsheet like datastuct
#row and colmns thought of as a dict of series

#constructing DataFrame
#common way is from a dict of equal length or a NumPy arrays
data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
      'year':[2000,2001,2002,2001,2002],
        'pop':[1.5,1.7,3.6,2.4,2.9]}
frame=DataFrame(data)

#if you want a specific sequence of colums you can specify
frametemp=DataFrame(data,columns=['year','state','pop'])
frame2=DataFrame(data,columns=['year','state','pop','debt'],
                 index=['one','two','three','four','five'])
#if you enter a non colm it will be nan
#one is also able to mark indecies
#you can access feature by using dot or ['year']