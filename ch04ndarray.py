# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 16:04:30 2016

Chapter 4 NumPy Basics

@author: Mahdi
"""
#creating a ndarry
import numpy as np
data1=[6,7.5,8,0,1]
arr1=np.array(data1)

#nested sequences will be multidim arrays
data2=[[1,2,3,4],[5,6,7,8]]
arr2=np.array(data2)

#getting dim of array
print(arr2.ndim)
print(arr2.shape)
