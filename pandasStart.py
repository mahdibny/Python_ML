# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:46:31 2016

Learning Pandas Chapter 5

@author: Mahdi
"""
from pandas import Series,DataFrame
import pandas as pd
import numpy as np

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
Constructing Series
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


"""""""""""""""""""""""
Constructing Data Frame
"""""""""""""""""""""""
#tabular, spreadsheet like datastuct
#row and colmns thought of as a dict of series

#constructing DataFrame
#common way is from a dict of equal length or a NumPy arrays
data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
      'year':[2000,2001,2002,2001,2002],
        'pop':[1.5,1.7,3.6,2.4,2.9]}
frame=DataFrame(data)
print(frame)

#if you want a specific sequence of colums you can specify
frametemp=DataFrame(data,columns=['year','state','pop'])
frame2=DataFrame(data,columns=['year','state','pop','debt'],
                 index=['one','two','three','four','five'])
print(frame2)
#if you enter a non colm it will be nan
#one is also able to make a name for indecies
#you can access feature by using dot or ['year']

#to retrieve a row you can use the ix method
print(frame2.ix['three']) #printing out a row with their colms

#setting values for debt
frame2['debt']=16.5
print(frame2)

frame2['debt']=np.arange(5.)
print(frame2)
#the list or arrays must match the lenght of the Frame
#if we use a series instead then the remaning index will hold nan
val=Series([-1.2,-1.5,-1.7],index=['two','four','five'])
frame2['debt']=val
print(frame2)

#if you assign a colm that dosent exist it will be create it.
#the del key world will delelte as with a dict
frame2['eastern']=frame2.state=='Ohio'
print(frame2)
del frame2['eastern']
print(frame2.columns)


#Another way to form a dataframe id by using nested dicts
pop={'Nevada':{2001:2.2,2002:2.9},'Ohio':{2000:1.5,2001:1.7,2002:3.6}}
frame3=DataFrame(pop)
print(frame3)
#one can transposee the data
frame3Trans=frame3.T
print(frame3Trans)

#the jeys in the inner dicts are unioned and sorted as index
#this int true if an explicit index is specified
frame3temp=DataFrame(pop,index=[2001,2002,2003])
print(frame3temp)

#Dicts of Series are treated similarly
pdata={'Ohio':frame3['Ohio'][:-1],'Nevada':frame3['Nevada'][:2]}
pdataFrame=DataFrame(pdata)
print(pdataFrame)

#There are more constructors in table 5.1
#if you have index.name and columns.name set it will look like
frame3.index.name='year'
frame3.columns.name='state'
print(frame3)
"""
state  Nevada  Ohio
year               
2000      NaN   1.5
2001      2.2   1.7
2002      2.9   3.6

"""

#value atrribute gives us data
print(frame3.values)


"""
Index Objects
"""
#index objects are responsible for holding the axis labels and other metadata

objI=Series(range(3),index=['a','b','c'])
indexI=objI.index
print(indexI)

#index objects are immutable and cannot be modified by user
indexI2=pd.Index(np.arange(3))
objI2=Series([1.5,-2.5,0],index=indexI2)

#in addition to being array like index also functions as a fixed-size set
print('Ohio' in frame3.columns)
print(2003 in frame3.index)

"""
Essential Functionality
"""

"""
Reindexing
"""
#reindex createa new object wth the data conformed to a new index
objRe=Series([4.5,7.2,-5.3,3.6],index=['d','b','a','c'])
print(objRe)
#calling reindex rearranges the data
objRe2=objRe.reindex(['a','b','c','d','e'])
print(objRe2)
#fill_value=0
objRe2=objRe.reindex(['a','b','c','d','e'],fill_value=0)
print(objRe2)

#ffill
obj3=Series(['blue','purple','yellow'],index=[0,2,4])
obj3.reindex(range(6),method='ffill')
print(obj3)

#with the dataframe reindex can alter either the row index, colums, or both
frameRe=DataFrame(np.arange(9).reshape((3,3)),index=['a','c','d'],columns=['Ohio','Texas','California'])
print(frameRe)

frameRe2=frameRe.reindex(['a','b','c','d'])
print(frameRe2)

#columns can be reindexed using columns keyword
statesRe=['Texas','Utah','California']
frameRe.reindex(columns=statesRe)

#interpolation
frameRe.reindex(index=['a','b','c','d'],method='ffill',columns=statesRe)
frameRe.ix[['a','b','c','d'],statesRe]

"""
Dropping entries from an axis
"""
#drop method
objDr=Series(np.arange(5.),index=['a','b','c','d','e'])
new_objDr=objDr.drop('c')
new_objDr2=objDr.drop(['d','c'])

dataDr=DataFrame(np.arange(16).reshape((4,4)),index=['Ohio','Colorado','Utah','New York'],columns=['one','two','three','four'])
dataDr.drop(['Colorado','Ohio'])

dataDr.drop('two',axis=1)
dataDr.drop(['two','four'],axis=1)

"""
Indexing, Selection, and filtering
"""
ObjInd=Series(np.arange(4.),index=['a','b','c','d'])
#one can slice these structures and set them to certain values using thier ind

#for Data Frames
dataINS=DataFrame(np.arange(16).reshape((4,4)),
                  index=['Ohio','Colorado','Utah','New York'],
                  columns=['one','two','three','four'])
print(dataINS)
print(dataINS['two'])
print(dataINS[['three','one']])

print(dataINS[:2]) #first two rows
print(dataINS[dataINS['three']>5]) #print where three value is >5

print(dataINS<5)
dataINS[dataINS<5]=0
print(dataINS) #data values change to 0 where true from previous command

#for data indexing on the rows we use ix enables one to select subset of rows
#and columns from DataFrame with NumPy like notation 
print(dataINS.ix['Colorado',['two','three']])
"""
Colorado Row values for cols two,three
output 
two      5
three    6
Name: Colorado, dtype: int32
"""
print(dataINS.ix[['Colorado','Utah'],[3,0,1]])
print(dataINS.ix[2]) #gets second index row
print(dataINS.ix[:'Utah','two']) #go till Utah get two cols

print(dataINS.ix[data.three>5,:3]) #get data where three is >5 and get 3 colms 

#many different ways inwhich one can manipulate data
