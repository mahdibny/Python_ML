# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 02:19:09 2016

@author: Mahdi
"""

#US Baby names 1880-2010
import pandas as pd
#creates data frame
names1880=pd.read_csv('names/yob1880.txt',names=['name','sex','birth'])
#groupbs by sex
names1880.groupby('sex').birth.sum()


#create a data frame with all data and create year colm
years=range(1880,2011)
pieces=[]
columns=['name','sex','births']

for year in years:
    path='names/yob%d.txt' %year
    frame=pd.read_csv(path,names=columns)
    frame['year']=year
    pieces.append(frame)
    #concatinage everything in to a single DataFrame
    names=pd.concat(pieces,ignore_index=True) # glues datafreame objects together
    #row wise by default
    #ignore b/c we are not inteested in preserving original row number 
    
#let us now aggreegate data at year and sex level
total_births=names.pivot_table('births',index='year',columns='sex',aggfunc=sum)
#what we do is sum the births make years the index and have colums of sex
"""
sex         F        M
year                  
1880    90993   110493
1881    91955   100748
1882   107851   113687
1883   112322   104632
1884   129021   114445
1885   133056   107802
1886   144538   110785

example

"""
total_births.tail() # gives the last values
total_births.plot(title='Total Birth by sex and year')

#now we want to add a prop value giving us a value that shows percent of names
#add a new column to each group
def add_prop(group):
    #integer division floords
    births=group.births.astype(float)
    group['prop']=births/births.sum()
    return group
    
names=names.groupby(['year','sex']).apply(add_prop)
# now we can verify that a prop colum sums up to one
#use np.allclose
import numpy as np
np.allclose(names.groupby(['year','sex']).prop.sum(),1)

#now we will create a subset of top1000 names for each sex.year combination
def get_top1000(group):
    return group.sort_index(by='births',ascending=False)[:1000]

grouped=names.groupby(['year','sex'])
top1000=grouped.apply(get_top1000)

#one could aslo
pieces=[]
for year,group in names.groupby(['year','sex']):
    pieces.append(group.sort_index(by='births',ascending=False)[:1000])
top1000=pd.concat(pieces,ignore_index=True)

"""
Analyzing Name Trends
"""
#split it into boys and girls
boys=top1000[top1000.sex=='M']
girls=top1000[top1000.sex=='F']

#pivot table for number of births by year and name
total_births=top1000.pivot_table('births',index='year',columns='name',aggfunc=sum)

#now we can plot this for a handful of names using pandas dataframe plot method
subset=total_births[['John','Harry','Mary','Marilyn']]
subset.plot(subplots=True,figsize=(12,10),grid=False,title="Number of births per year")

"""
Measuring increase in name diversity
"""
table=top1000.pivot_table('prop',index='year',columns='sex',aggfunc=sum)
table.plot(title='Sum of table1000.prop by year and sex',yticks=np.linspace(0,1.2,13),xticks=range(1880,2020,10))
#table shows increase in name diversity 

#lets see if we can find number of distinct names
#taking just boys
df=boys[boys.year==2010]
#now sorting propr in decending order how many of most pop names does it take
#to reach 50%
prop_cumsum=df.sort_index(by='prop',ascending=False).prop.cumsum()

df=boys[boys.year==1900]
in1900=prop_cumsum=df.sort_index(by='prop',ascending=False).prop.cumsum()
in1900.searchsorted(.5)+1

def get_quantile_count(group,q=.5):
    group=group.sort_values(by='prop',ascending=False)
    return group.prop.cumsum().searchsorted(q)+1

diversity=top1000.groupby(['year','sex']).apply(get_quantile_count)
diversity=diversity.unstack('sex')
diversity.head()

diversity.plot(title="number of popular names in to 50%")
