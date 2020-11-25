import numpy as np
import sys

a = np.array([(2,3),(3,2)])
print(type(a))
print("dimention = ",a.ndim)
print("getsizeof = ",sys.getsizeof([]))#size of empty
print("itemsize = ",a.itemsize)
print("dtype = ",a.dtype)

c = np.array([(10,20,22),(44,11,33)])
print("size = ",c.size)#gives total number of ele
print("shape = ",c.shape)
print("dtype = ",c.dtype)

print("2 by 3 array = \n",c)
c = c.reshape(3,2)
print("3 by 2 array = \n",c)

print("c[0][1] = ",c[0][1]) #[0,4] it gives indexerror
print("c[1][1] = ",c[1][1])
print("c[2][1] = ",c[2][1])

c = np.array([(10,20),(44,11),(22,33)])
print(c)
print("ele of second column",c[0:,1])

print("minimum = ",c.min())
print("maximum = ",c.max())

d = np.array([(144,196),(36,49),(100,4)])
print(np.sqrt(d))

e = np.array([(1,2),(3,4),(5,6)])
print("sum of rows = ",e.sum(axis=1))
print("sum of column = ",e.sum(axis=0))