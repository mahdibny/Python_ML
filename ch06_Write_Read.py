# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 02:25:30 2016

Chapter 6: Data Loading, Storage, and File Formats

inputs and outputs with panda objects

@author: Mahdi
"""





"""
Reading and Writing Data in Text Format


pg 155
Parsing Function in pandas
read_csv Load delimited data from a file, URL, or file-like object. Use comma as default delimiter
read_table Load delimited data from a file, URL, or file-like object. Use tab ('\t') as default delimiter
read_fwf Read data in fixed-width column format (that is, no delimiters)
read_clipboard Version of read_table that reads data from the clipboard. Useful for converting tables from web pages

"""
from pandas import Series, DataFrame
import pandas as pd
df=pd.read_csv('../pydata-book/ch06/ex1.csv')
#or use read_table and use delimeter
pd.read_table('../pydata-book/ch06/ex1.csv',sep=',')

#consider a file you can create column names
df1=pd.read_csv('../pydata-book/ch06/ex2.csv',header=None)
df2=pd.read_csv('../pydata-book/ch06/ex2.csv',names=['a','b','c','d','message'])
# above line we ccreate and choose specific column names

names=['a','b','c','d','message']
df3=pd.read_csv('../pydata-book/ch06/ex2.csv',names=names,index_col='message')
#format data so messages become columns

#Hierachical indexing 
parse=pd.read_csv('../pydata-book/ch06/csv_mindex.csv',index_col=['key1','key2'])
print(parse)

#whitespace delimiter
result=pd.read_table('../pydata-book/ch06/ex3.txt',sep='\s+')
print(result)

#skip rows
df4=pd.read_csv('../pydata-book/ch06/ex4.csv',skiprows=[0,2,3])
print(df4)

#handling missing data
result_1=pd.read_csv('../pydata-book/ch06/ex5.csv')
print(result_1)
#do things that we talk about in pandas

'''
Table 6.2 pg 160
'''


"""
Reading Text Files in Pieces
"""
results_2=pd.read_csv('../pydata-book/ch06/ex6.csv')
print(results_2)
#read out a small numbers of rows
results_3=pd.read_csv('../pydata-book/ch06/ex6.csv',nrows=5)
print(results_3)

#to read in pieces specify a chunksize as a number of rows
chunker=pd.read_csv('../pydata-book/ch06/ex6.csv',chunksize=1000) #text parser object
tot=Series([])
for pieces in chunker:
    tot=tot.add(pieces['key'].value_counts(),fill_value=0)

tot=tot.order(ascending=False)

"""
Writing Data Out to Text Format
"""
