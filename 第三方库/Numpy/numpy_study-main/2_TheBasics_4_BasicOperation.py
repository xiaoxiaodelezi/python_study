# 基本操作

#算数运算对于数组都是基本操作。numpy会创建一个新的数组并填充运算结果

import numpy as np

a=np.array([20,30,40,50])
b=np.arange(4)

print(b)
# [0 1 2 3]

c=a-b
print(c)
# [20 29 38 47]

print(b**2)
# [0 1 4 9]

print(10*np.sin(a))
# [ 9.12945251 -9.88031624  7.4511316  -2.62374854]

print(a<35)
# [ True  True False False]


#和其他矩阵语言不同，矩阵相乘在numpy中是基本操作。在numpy中可以使用@或者dot函数
A=np.array(
    [[1,1],
    [0,1]]
)
B=np.array(
    [[2,0],
    [3,4]]
)

print(A*B)
# [[2 0]    #A*B   A11*B11,A21*B21,A21*B21,A22*B22
#  [0 4]]

print(A@B)
# [[5 4] #矩阵相乘
#  [3 4]]

print(A.dot(B))
# [[5 4] #矩阵相乘
#  [3 4]]



#其他一些操作，比如+=,*=，会更改原始数据，而不创建先的数列

rg=np.random.default_rng(1)#numpy.random.default_range()
a=np.ones((2,3),dtype=int)
b=rg.random((2,3))

print(a)
# [[1 1 1]
#  [1 1 1]]

print(b)
# [[0.51182162 0.9504637  0.14415961]
#  [0.94864945 0.31183145 0.42332645]]

a *=3
print(a)
# [[3 3 3]  #a改变了
#  [3 3 3]]

b+=a
print(b)
# [[3.51182162 3.9504637  3.14415961]  #b改变
#  [3.94864945 3.31183145 3.42332645]]

# a+=b  #会发生错误，因为a的数据类型是整数，加上浮点数后重新存入a时会发生数据类型不同，发生错误
# Traceback (most recent call last):
#   File "D:/Study/Python/numpy/test.py", line 76, in <module>
#     a+=b
# numpy.core._exceptions.UFuncTypeError: Cannot cast ufunc 'add' output from dtype('float64') to dtype('int32') with casting rule 'same_kind'


import math #为了表示pi
a=np.ones(3,dtype=np.int32)
b=np.linspace(0,math.pi,3) #[start,end] 总共分成3个数

print(b.dtype.name)
# float64

c=a+b
print(c)
# [1.         2.57079633 4.14159265]

print(c.dtype.name)
# float64


d=np.exp(c*1j)
print(d)
# [ 0.54030231+0.84147098j -0.84147098+0.54030231j -0.54030231-0.84147098j]

print(d.dtype)
# complex128


#一些一元运算，比如计算数组长所有元素的和，也能在ndarray的类中使用类似方法
a=rg.random((2,3))

print(a)
# [[0.82770259 0.40919914 0.54959369]
#  [0.02755911 0.75351311 0.53814331]]

print(a.sum())
#3.1057109529998157

print(a.min())
#0.027559113243068367

print(a.max())
#0.8277025938204418


#通常这些操作都会直接作用于数组就像它时一个数字的列表，而不在乎它的形状。但是，通过给与轴的参数，
#可以对于数组中指定的轴的操作

b=np.arange(12).reshape(3,4)
print(b)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(b.sum(axis=0)) #列的总和
# [12 15 18 21]

print(b.min(axis=1))#行中最小的值
# [0 4 8]

print(b.cumsum(axis=1))#按照行，每个数字等于前面数字和自己的累加
# [[ 0  1  3  6]
#  [ 4  9 15 22]
#  [ 8 17 27 38]]


#numpy提供类似数学的函数，比如sin，cos，和exp。在numpy中，这些被称为整体化函数（ufunc）。
#在numpy中，这些函数会在数列的元素上计算呢，创建一个数组输出。

B=np.arange(3)

print(B)
# [0 1 2]

print(np.exp(B))
# [1.         2.71828183 7.3890561 ]

print(np.sqrt(B))
# [0.         1.         1.41421356]

C=np.array([2.,-1.,4.])
print(np.add(B,C))
# [2. 0. 6.]


# 相关函数
# all
# any
# apply_along_axis
# argmax
# argmin
# argsort
# average
# bincount
# ceil
# clip
# conj
# corrcoef
# cov
# cross
# cumprod
# cumsum
# diff
# dot
# floor
# inner
# invert
# lexsort
# maximum
# mean
# median
# mimimum
# nonzero
# outer
# prod
# re
# round
# sort
# std
# sum
# trace
# transpose
# var
# vdot
# vectorize
# where

