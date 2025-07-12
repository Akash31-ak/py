import numpy as np
a = np.array([1,2,3])
b = np.array(42)
c = np.array([[1,2],[3,4]])
d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
#check the dimension of the array
print(a.ndim)
print(a)
#ndmin is used to define the dimension of the array 
arr = np.array([1,2,3,4], ndmin=5)
print(arr.ndim)
print(arr.dtype)
print(c.ndim)
#indexing
print(c[1,0])
print(d[0,1,1])
print(d[0,1,2])
print(d[1,0,0])
print(d[1,1,1])
#slicing operation(a1[start:end:step])
a1 = np.array([1,2,3,4,5,6,7,8,9])
print(a1[0:6:2])
#slicing of 2d array 
c1 = np.array([[1,2,5,6,7],[3,4,8,9,10]])
print(c1[1,1:4])#slice elements from 1 to 4 index in the index1 of the array 
print(c1[0:2,2])#returns index 2 from both the elements in the array
print(c1[0:2,1:4])#slice elements from 1 to 4 index in the array for all elements
print(c1.shape)

#common Creators in numpy
np.zeros((2,3))#2x3 array of zeros
np.ones((3,))#1d array of 3 elements
np.eye(3)#identity matrix
print(np.arange(1,10,2))#creats values from 1 to 9 (excluding 9 ),in steps of 2
print(np.linspace(0,1,5))
#reshape array
d1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
d2 = d1.reshape(2,6)
print(d2)

arr2 = np.array([[1,2,3,4],[3,4,5,6]])
#arr3 = arr2.reshape()
print(arr2.reshape(8,))
print(arr2.reshape(1,8))
#flatten method used to directly convert 2d array to 1d array
print(arr2.flatten())


x = np.array([1,2,3])
y = np.array([4,5,6])
print(x+y)
print(x*2)
print(np.sqrt(x))
#broadcasting operator
x1 = np.array([10,20,30])
y1 = np.array([[1],[2],[3]])
print(x1+y1)

z = np.array([[1,2],[3,4]])
print(z.sum())
print(z.max(axis=0))#finds max value in each column
print(z.mean())
print(np.median(z))

#boolean indexing and masking
z1 = np.array([1,2,3,4,5,6,7,8,9])
mask = z1%2==0
print(z1[mask])

marks = np.array([29,45,38,22,88,97,67,75,])
marks = marks+5
mask = marks<=35
print(marks[mask])

#pandas-
#installl pandas = py -m pip install pandas








