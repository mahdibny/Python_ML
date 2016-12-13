# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 18:10:40 2016

@author: Mahdi
"""

path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
import json 
records = [json.loads(line) for line in open(path)]

from pandas import DataFrame, Series
import pandas as pd
frame = DataFrame(records)
# create a frame from the usa data
# next line shows the most used time zones in cell 'tz'
frame['tz'][:10]

#filling in the unknown values for missing tone zone data in records
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz=='']='Unknown'
tz_counts=clean_tz.value_counts()
tz_counts[:10]

#makes a matlab plot of 
tz_counts[:10].plot(kind='barh',rot=0)

frame['a'][1]
frame['a'][50]
frame['a'][51]

results=Series([x.split()[0] for x in frame.a.dropna()])
results[:5]
results.value_counts()[:8]


import numpy as np
# decompose toptime zones into windows and non windos
# if a string has windows then windows user
# remove the missing data
cframe=frame[frame.a.notnull()]
# then see if frame has windows in each row
operating_system=np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
operating_system[:5]
#then group the data by time zone and operating system
by_tz_os=cframe.groupby(['tz',operating_system])

agg_counts=by_tz_os.size().unstack().fillna(0)
agg_counts[:10]

#select top overall timezone construct an indirect index array from the row colms in agg counts
indexer=agg_counts.sum(1).argsort()
indexer[:10]
count_subset=agg_counts.take(indexer)[-10:]
count_subset

# ploting this data as a stacked bar plot

count_subset.plot(kind='barh',stacked=True)
# not easy to see realitive percentage so we normalize
normed_subset=count_subset=count_subset.div(count_subset.sum(1),axis=0)
normed_subset.plot(kind='barh',stacked=True)
