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
arrD=np.arange(10)
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
print(arr2d[0,2]) #same thing as above

arr3d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d)
print(arr3d[0]) #the 3x2 matrix

old_values=arr3d[0].copy()

arr3d[0]=64 #change these values to 64
print(arr3d)

arr3d[0]=old_values
print(arr3d)

#more slicing
print(arr2d[:2]) #1 and 2 row in matrix

print(arr2d[:,2]) #prints by colums

print(arr2d[:2,1:]) #first 0 1 row and from 1index colm onward
print(arr2d[1,:2]) #1 index row and first 2 col
print(arr2d[2,:1]) #2 index row and first col

print(arr2d[:,:1]) #print all rows first col

"""Boolean Indexing"""
names=np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
data=np.random.rand(7,4);
print(names)
print(data)

print(names=='Bob') #prints an array seeing which elements equal Bob
print(data[names=='Bob']) #what happens is it prints the index where true
print(data[names=='Bob',2:]) #rows where Bob index true and then from cols 2 on
print(data[names=='Bob',3]) #rows """" and 3index

names !='Bob'
print(names)
print(data[-(names=='Bob')]) #- same as !
#can also do names!=Bob

mask=(names=='Bob') | (names=='Will')
print(mask)
data(mask)

#Selecting data from an array by boolean indexing always creates a copy of the 
#data, even if the returned array is unchanged.
# also and and or

#lets set all negative values 0
data[data<0]=0
print(data)

#set where ever !==Joe =7
data11=data[names!='Joe']=7
print(data11)

"""Fancy Indexing"""
#term to describe indexing using integer arrays
fancyArr=np.empty((8,4))
for i in range(8):
    fancyArr[i]=i
print(fancyArr)

#selecting subsets rows by index
print(fancyArr[[4,3,0,6]])
print(fancyArr[[-3,-5,-7]]) #going backwards

#reshaping ans indexing
arrF=np.arange(32).reshape((8,4)) #normaly 1D but reshaped
print(arrF)
print(arrF[[1,5,7,2],[0,3,1,2]]) #prints row then index at that row

print(arrF[[1,5,7,2]][:,[0,3,2,1]])
#prints the rows, then from 0 index,3 index 2,1 cols

#another way to do this
print(arrF[np.ix_([1,5,7,2],[0,3,1,2])])

"""Transposing and Swapping Axes"""
arrT=np.arange(15).reshape((3,5))
arrayTranspose=arrT.T

#XTX using np.dot
Tarr=np.random.rand(6,3)
print(np.dot(Tarr.T,Tarr))

#higher dimensions
arrTr=np.arange(16).reshape((2,2,4))
print(arrTr)
print(arrTr.transpose((1,0,2)))

"""
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7]],

       [[ 8,  9, 10, 11],
        [12, 13, 14, 15]]])

after rearranged
array([[[ 0,  1,  2,  3],
        [ 8,  9, 10, 11]],

       [[ 4,  5,  6,  7],
        [12, 13, 14, 15]]])
"""

#swapaxes
print(arrTr.swapaxes(1,2))
#tranpose each individual matrices
"""
array([[[ 0,  4],
        [ 1,  5],
        [ 2,  6],
        [ 3,  7]],

       [[ 8, 12],
        [ 9, 13],
        [10, 14],
        [11, 15]]])

"""


