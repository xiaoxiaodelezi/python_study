#索引进阶和索引技巧

#numpy可以提供比python序列更多的索引工具。
#除了以整数和切片方式索引，如我们所见，数组可以通过整数数组和布尔数组索引。

import numpy as np

#ndarray可以直接运算，运算会作用于所有元素
a=np.arange(12)**2
print(a)
# [  0   1   4   9  16  25  36  49  64  81 100 121]

i=np.array([1,1,3,8,5])
print(a[i]) #通过数组参数索引
# [ 1  1  9 64 25]

#注意这里j也是一个ndarray
#a[ndarray]将会将a的元素按照j的排列方式返回，其中的值为a的对应j值
j=np.array([[3,4],[9,7]])
print(a[j]) #a的元素按照j数组方式排列，值为a中索引值为j的数值
# [[ 9 16]
#  [81 49]]

#当被索引的数组是个多维数组，单个的索引数组关联到a的第一个维度。下面的例子是一个关于如何使用调色板将
#一张图片标签转为一张彩色图片

palette=np.array([
    [0,0,0],    #black
    [255,0,0],  #red
    [0,255,0],  #green
    [0,0,255],  #blue
    [255,255,255]   #white
])

#单个索引关联到palette的第一维度，也就是列
image=np.array([
    [0,1,2,0],
    [0,3,4,0]
])
print(palette[image])   #(2,3,4)彩色画面
# [[[  0   0   0]   #palette[0]
#   [255   0   0]   #palette[1]
#   [  0 255   0]   #palette[2]
#   [  0   0   0]]  #palette[0]
#
#  [[  0   0   0]   #palette[0]
#   [  0   0 255]   #palette[3]
#   [255 255 255]   #palette[4]
#   [  0   0   0]]] #palette[0]


#我们可以索引超过一个维度。对每个维度的索引数组必须有相同的形状。
#i和j的相同位置组成a索引值，然后放在对应的位置
a=np.arange(12).reshape(3,4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

i = np.array([   #a的第一个维度
    [0,1],
    [1,2]
])

j=np.array([    #a的第二个维度
    [2,1],
    [3,3]
])

print(a[i,j]) #i和j必须拥有相同的形状
# [[ 2  5]   #a[i00 j00] a[i01 j01]
#  [ 7 11]]  #a[i10 j10] a[i11 j11]

print(a[i,2])
# [[ 2  6]
#  [ 6 10]]

print(a[:,j])  #a是（3，4），第一个切片，表示a第一个维度的每个元素，也就是3个，j表示对每个第一维度的元素去j索引的值
# [[[ 2  1]
#   [ 3  3]]
#
#  [[ 6  5]
#   [ 7  7]]
#
#  [[10  9]
#   [11 11]]]


#在python中，arr[i,j]和arr[(i,j)]含义完全一致，所以在numpy中，我们可以给i和j赋值一个元组，然后做索引
l=(i,j)
print(a[l]) #意义和a[i,j]一致
# [[ 2  5]
#  [ 7 11]]


#但是我们不能把i和j存入一个数组，因为这个数组会被解释为对于a的第一个维度的索引
s=np.array([i,j])
# print(a[s])
# Traceback (most recent call last):
#   File "D:/Study/Python/numpy/test.py", line 94, in <module>
#     print(a[s])
# IndexError: index 3 is out of bounds for axis 0 with size 3



print(a[tuple(s)]) #可以把s元组化，然后作为a的索引参数
# [[ 2  5]
#  [ 7 11]]


#另一个常用的利用数组作为索引条件的是寻找时间相关的最大值

time=np.linspace(20,145,5)  #时间刻度
data=np.sin(np.arange(20)).reshape(5,4)  #4个时间相关的系列
print(time)
# [ 20.    51.25  82.5  113.75 145.  ]
print(data)
# [[ 0.          0.84147098  0.90929743  0.14112001]
#  [-0.7568025  -0.95892427 -0.2794155   0.6569866 ]
#  [ 0.98935825  0.41211849 -0.54402111 -0.99999021]
#  [-0.53657292  0.42016704  0.99060736  0.65028784]
#  [-0.28790332 -0.96139749 -0.75098725  0.14987721]]

ind=data.argmax(axis=0) #axis=0 表示垂直方向
print(ind)
# [2 0 3 1]

time_max=time[ind]
print(time_max)
# [ 82.5   20.   113.75  51.25]

data_max=data[ind,range(data.shape[1])]  #本质是data然后[数组1，数组2]的切片
print(data_max)
# [0.98935825 0.84147098 0.99060736 0.6569866 ]

print(np.all(data_max==data.max(axis=0)))
# True


#你也可以用一个索引数组作为目标
a=np.arange(5)
print(a)
# [0 1 2 3 4]
a[[1,3,4]]=0 #用一个列表作为索引，a的所有列表中的索引值都赋值0
print(a)
# [0 0 2 0 0]


#但是当索引列表中的数据有重复，指定值会多次计算，并留下最终值

a=np.arange(5)
print(a)
# [0 1 2 3 4]
a[[0,0,2]]=[1,2,3]
print(a) #a0被赋值两次，1和2，最终值为2
# [2 1 3 3 4]

#
#这是合理的，但是当你使用python下的+=时，输出结果可能不是预期的
a=np.arange(5)
a[[0,0,2]]+=1 #在这里+=只会被计算一次，特别需要注意
print(a)
# [1 1 3 3 4]
#虽然a0被调用2次，但是只被加了1此，这是由于python要求a+=1 等于a=a+1

