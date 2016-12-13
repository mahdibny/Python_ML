# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 20:06:22 2016

@author: Mahdi
"""

#movielens 1D dataset
import pandas as pd
unames=['user_id','gender','age','occupation','zip']
users=pd.read_table('users.dat',sep='::', header=None, names=unames)
users[:5]

rnames=['user_id','movie_id','rating','timestamp']
ratings=pd.read_table('ratings.dat',sep='::',header=None, names=rnames)
ratings[:5]

mnames=['movie_id','title','genres']
movies=pd.read_table('movies.dat',sep='::',header=None, names=mnames)
movies[:5]

#pandas merge function
data=pd.merge(pd.merge(ratings,users),movies)
data
data.ix[0]

mean_ratings=data.pivot_table('rating',index='title',columns='gender',aggfunc='mean')
#this creates dataframes that has mean ratings with mive totals as row labels and gender as col
#now filter these with ratings of only 250 ratings 
ratings_by_title=data.groupby('title').size()
ratings_by_title[:10]

active_titles=ratings_by_title.index
#index can be used to select rows from mean rating
mean_ratings=mean_ratings.ix[active_titles]
mean_ratings
#now we can sort to see top films amoung female viewers
top_female_ratings=mean_ratings.sort_index(by='F',ascending=False)
top_female_ratings[:10]

"""
    Measuring rating disagreement
"""

#now lets say we want to find the most disisive measurments bt male and female
#one way is to find a difference rating
mean_ratings['diff']=mean_ratings['M']-mean_ratings['F']
sorted_by_diff=mean_ratings.sort_index(by='diff')
sorted_by_diff[:15]
#reverse the sorting order
sorted_by_diff[::-1][:15]

#now we want to find the most disagreement regardless of gender
#we can measure this by findint the standard deviation or variance 
rating_std_by_title=data.groupby('title')['rating'].std()
#filter down to active titiles
rating_std_by_title=rating_std_by_title.ix[active_titles]
#order series by descending order
rating_std_by_title.order(ascending=False)[:10]