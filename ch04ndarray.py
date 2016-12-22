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
print(data[mask])

#Selecting data from an array by boolean indexing always creates a copy of the 
#data, even if the returned array is unchanged.
# also and and or

#lets set all negative values 0
data[data<0]=0
print(data)

#set where ever !==Joe =7
#data[names!='Joe']=7
#print(data11)

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

"""
Universal Functions: Fast Element-wise Array Functions
ufunc - funct that performs elementwise operations on 
data in ndarrays.
"""
#sqrt and exp function
arrUF=np.arange(10)
print(np.sqrt(arrUF))
print(np.exp(arrUF))

#these are the unary functs
#there are two binasy ufuncts like add and maxium using 2 arrays

x=np.random.randn(8)
y=np.random.randn(8)
print(x)
print(y)

max_xy=np.maximum(x,y)
print(max_xy)

#some ufunct can retrutn multiple arrays
#arrays.modf divmod returns the fractional and integral parts a floating point
#array
arrDf=np.random.randn(7)*5
print(np.modf(arrDf))


""""
Data Processing Using Arrays
"""
#vectorization instead of for loops
points=np.arange(-5,5,0.01)
xs,ys=np.meshgrid(points,points)

import matplotlib.pyplot as plt
z=np.sqrt(xs**2+ys**2)
plt.imshow(z,cmap=plt.cm.gray)
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2+y^2}$ for a grid of values")

"""
Expressing Conditional Logic as Array Operations 
"""
#numpy.where vectorized version of the ternary expression x
# if condition else y
xarr=np.array([1.1,1.2,1.3,1.4,1.5])
yarr=np.array([2.1,2.2,2.3,2.4,2.5])
cond=np.array([True,False,True,True,False])

#suppose we want to take a value from xarr when cond is True
#otherwise use False

result=[(x if c else y) for x,y,c in zip(xarr,yarr,cond)]
print(result)
#lots of problems can happen not very large arrays
# np.where
result=np.where(cond,xarr,yarr)
#the second and third arguments can be scalars too

arrWh=np.random.randn(4,4)
arrWh1=np.where(arrWh>0,2,-2)
arrWh2=np.where(arrWh>0,2,arrWh)
print(arrWh)
print(arrWh1)
print(arrWh2)


#arrays passed in wheres can be more than just equal sized arrays

"""
Mathematical and Statistical Methods
"""
#many statiscal methods are availible 
arrSt=np.random.rand(5,4) #normally distributed data
print(arrSt.mean())
print(np.mean(arrSt))
print(arrSt.sum())
# mean and sum have optional axis arguments so one can get sum and 
#mean from a specific dimension of the array
print(arrSt.mean(axis=1))
print(arrSt.sum(0))

#methods like cumsum and cumprod do not aggregate, produce arra of inter results
arrSt1=np.array([[0,1,2],[3,4,5],[6,7,8]])
print(arrSt1.cumsum(0))
print(arrSt1.cumprod(1))

"""
Methods for Boolean Arrays
"""
#boolean values are 0,1 the sum is often used as a means of counting True/False
arrB=np.random.rand(100)
print((arrB>0).sum())

#any and all, see if all values true and if any true in array
bools=np.array([False,False,True,False])
print(bools.any())
print(bools.all())

"""
Sorting
"""
#NumPy can be sorted inplace using sort methods
arrSo=np.random.rand(8)
print(arrSo)
arrSo.sort()
print(arrSo)

#multidimensional arrays can have each ID dection of values sorted in place
#along axi by passing the asis number to sor
arrSo1=np.random.rand(5,3)
print(arrSo1)
arrSo1.sort(1)
print(arrSo1)
#np.sort retuens copy of sorted array instead of inplace sort or is it

"""
Unique and Other Set Logic
"""
names1=np.unique(names)
print(names1)

#pure python alternative
print(sorted(set(names)))

#np.ind1d test membership of valuees in one array to another
values=np.array([6,0,0,3,2,5,6])
print(np.in1d(values,[2,3,6]))

"""
File Input and Output with Arrays
"""
#NumPy is able to save and load data to and from disk in text or binary format
#np.save np.load
arrfi=np.arange(10)
np.save('some_array',arrfi)
np.load('some_array.npy')

#zip files np.savez 

"""
Saving and Loading Text Files
"""
#np.loadtxt
#np.genfromtxt
arrSL=np.loadtxt('array_ex.txt',delimiter=',')
print(arrSL)
#np.savetxt

"""
Linear Algebra
"""
xLA=np.array([[1.,2.,3.],[4.,5.,6.]])
yLA=np.array([[6.,23.],[-1,7],[8,9]])
print(xLA)
print(yLA)
xLA.dot(yLA)
np.dot(xLA,yLA)
print(xLA.dot(yLA))
print(np.dot(xLA,yLA))

from numpy.linalg import inv,qr
X=np.random.randn(5,5)
mat=X.T.dot(X)
print(np.dot(xLA,yLA))

print(X)
print(mat)

inv(mat)
print(inv(mat))
mat.dot(inv(mat))
print(mat.dot(inv(mat)))

q,r=qr(mat) #qr decomposition
print(r)

"""
Random Number Generation
"""
#normal
samples=np.random.normal(size=(4,4))
from random import normalvariate
N=1000000
"""
run code for times
"""
#timeit samples = [normalvariate(0,1) for _ in xrange(N)]
#timeit np.random.normal(size=N)

"""
Example: Random Walks
"""
#simulation of random walks
import random
position=0
walk=[position]
step=1000
for i in xrange(step):
    step=1 if random.randint(0,1) else -1
    position += step
    walk.append(position)

#np.random module to draw 1,000 coin     
nsteps=1000
draws=np.random.randint(0,2,size=nsteps)
steps=np.where(draws>0,1,-1)
walk=steps.cumsum()
#extract statistics like the min and max value
print(walk.min())
print(walk.max())

#first crossing time, the step at which rand walk reaches a particular value
#10 steps away from origin in either direction
print((np.abs(walk)>=10).argmax())

"""
Simulationg Many Random Walks at Once
"""
