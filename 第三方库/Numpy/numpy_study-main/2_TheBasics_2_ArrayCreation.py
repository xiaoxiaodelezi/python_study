#这里介绍了几个创建数组的方式

import numpy as np

#你可以通过使用数列函数从一个常规的python列表或者元组中创建。生成的数列类型是来自于元素在原始数据的状况。

a=np.array([2,3,4]) #导入一个python列表
print(a)
#[2 3 4]
print(a.dtype) #数据类型是和源列表一致
#int32
b=np.array([1.2,3.5,5.1])
print(b)
# [1.2 3.5 5.1] #源数据是浮点数，numpy的数列中也是。
print(b.dtype)
# float64


#传入多个参数从而发生错误的情况非常常见。
# a=np.array(1,2,3,4) #错误，参数导入错误。
# Traceback (most recent call last):
#   File "D:/Study/Python/numpy/test.py", line 21, in <module>
#     a=np.array(1,2,3,4)
# TypeError: array() takes from 1 to 2 positional arguments but 4 were given


#数组将序列中的序列转换成一个二维数组，序列中的序列中的序列将会被转为一个三维数组，以此类推
b=np.array([(1.5,2,3),(4,5,6)]) #列表和元组都会被认为是序列，这个是一个列表中有两个元组。
print(b)
# [[1.5 2.  3. ]
#  [4.  5.  6. ]]

#创建数组时可以设定数据类型
c=np.array([[1,2],[3,4]],dtype=complex) #通过dtype来设定数据类型
print(c)
# [[1.+0.j 2.+0.j]
#  [3.+0.j 4.+0.j]]

#经常在创建数组的时候，不知道数据的数值，但是却知道数组的大小。因此nunpy提供了多个函数来初始化创建的
# 数组的初始值。这些将会最小化增加数组的需求，因为增加数组将会是一个很消耗资源的操作。

# 函数zeros创建一个全部都是0的数组，ones创建一个全部都是1的数组，empty创建一个初始值随机的数组（值取决于内存）。
# 默认情况下，创建的时float64形式，不过可以通过dtype来改变。

print(np.zeros((3,4))) #注意双括号(3,4)是一个参数
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

print(np.ones((2,3,4),dtype=np.int16))

# [[[1 1 1 1]
#   [1 1 1 1]
#   [1 1 1 1]]
#
#  [[1 1 1 1]
#   [1 1 1 1]
#   [1 1 1 1]]]

print(np.empty((2,3),dtype=np.int16)) #py运算值并不随机，为0
# [[1.39069238e-309 1.39069238e-309 1.39069238e-309]
#  [1.39069238e-309 1.39069238e-309 1.39069238e-309]]

print(np.arange(10,30,5))#arange [start,end) step=5
#[10 15 20 25]

print(np.arange(0,2,0.3))
# [0.  0.3 0.6 0.9 1.2 1.5 1.8]



# 相关函数
# array
# zeros
# zeros_like
# ones
# ones_lie
# empty
# empty_like
# arange
# linspace
# fromfuncition
# fromfile
