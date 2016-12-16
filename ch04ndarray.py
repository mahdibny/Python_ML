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
print(arr2.dtype)

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
print(float_arr.dtype)

#if you have an array of strings that need
#to be converted to number you can use this
#method to convert
numeric_strings=np.array(['1.25','-9.6','42'],dtype=np.string_)
numeric_strings.astype(float)
#as type always create a new arrat even if the new dtype is the
#same as the old
print("Here")
"""
Operations between arrays and scalars
"""
#most of the operations here are element wise
arrn=np.array([[1.,2.,3.],[4.,5.,6.]])
print(arrn)
arrOp=arrn*arrn
print(arrOp)
arrOp1=arrn-arrn
print(arrOp1)
#scalar multiplaction also works
arrOp2=1/arrn
print(arrOp2)
arrOp3=arrn**0.5
print(arrOp3)

#Chapter 12 is called broadcasting 

"""
Basic Indexing and Slicing
"""
arrD=np.arrange(10)
print(arrD)
print(arrD[5])
print(arrD[5:8])
arrD[5:8]=12 #assign  elements 5-8 =12
print(arrD)

'''data is not copied  the array source is changed'''

arr_slice=arrD[5:8]
arr_slice[1]=12345 # the 1 index element to the value
print(arrD)

arr_slice[:]=64 #everyelement in arr_slice  =64
print(arrD)

#higher dimension array
arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d)
print(arr2d[2]) #2nd index row 7,8,9

print(arr2d[0][2]) #2nd index element in 0index row 3
