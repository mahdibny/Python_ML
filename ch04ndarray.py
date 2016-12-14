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
print("dimension of array " + arr2.ndim)
print("shape of array " + arr2.shape)
print("data type of array " + arr2.dtype)

#sometimes np.zeroes returns grabage
#there is also a ones command
#also an empty command where there are no values
#eyes for identity
arrempty=np.zeros(10)
arrempty2=np.zeros((3,6))
arrempty3=np.zeros((2,3,2))

#arange is an array-valued version of
#the built in Python range function

arr3=np.arange(15)

#one can also say the data type of the array
arr1=np.array([1,2,3],dtype=np.float64)
arr2=np.array([1,2,3],dtype=np.int32)

#you can convert/cast to different data types
arr=np.array([1,2,3,4,5])
float_arr=arr.astype(np.float64)
print("new type "+float_arr.dtype)

#if you have an array of strings that need
#to be converted to number you can use this
#method to convert
numeric_strings=np.array(['1.25','-9.6','42'],dtype=np.string_)
numeric_strings.astype(float)
#as type always create a new arrat even if the new dtype is the
#same as the old

"""
Operations between arrays and scalars
"""
