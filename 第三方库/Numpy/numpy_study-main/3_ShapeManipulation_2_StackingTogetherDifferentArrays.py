#不同数组的叠加

import numpy as np

#不同的数组可以在各自不同的维度上叠加

rg=np.random.default_rng(1)
a=np.floor(10*rg.random((2,2)))
print(a)
# [[5. 9.]
#  [1. 9.]]

b=np.floor(10*rg.random((2,2)))
print(b)
# [[3. 4.]
#  [8. 4.]]

print(np.vstack((a,b))) #垂直方向
# [[5. 9.]
#  [1. 9.]
#  [3. 4.]
#  [8. 4.]]

print(np.hstack((a,b))) #水平方向
# [[5. 9. 3. 4.]
#  [1. 9. 8. 4.]]

#函数column_stack

from numpy import newaxis
print(np.column_stack((a,b)))#a,b都是二维的时候,相当于hstack
# [[5. 9. 3. 4.]
#  [1. 9. 8. 4.]]

a=np.array([4.,2.])
b=np.array([3.,8.])
print(np.column_stack((a,b)))#a,b都是一维的时候,相当于增加了一个维度,在这个维度中包含a和b两个元素
# [[4. 3.]
#  [2. 8.]]
print(np.hstack((a,b))) #区别于column_stack
# [4. 2. 3. 8.]

print(a[:,newaxis])#将a看成是一个一维的列向量,本质是水平向垂直翻转
# [[4.]
#  [2.]]

print(np.column_stack((a[:,newaxis],b[:,newaxis])))#同时将a,b翻转,这时a,b都是(1,2)的数组,列叠加,成为了(2,2)
# [[4. 3.]
#  [2. 8.]]

print(np.hstack((a[:,newaxis],b[:,newaxis])))#这种二维的水平叠加,hstack和column_stack结果相同
# [[4. 3.]
#  [2. 8.]]

#row_stack函数和vstack函数对于任何输入的数组都有相同作用,两者一致

print(np.column_stack is np.hstack)
# False
print(np.row_stack is np.vstack)
# True

#一边拿来说,在超过二维的数组中,hstack根据他们的第二个轴变化,vstack根据第一个轴变化,concatenate根据输入的参数
a=np.floor(10*rg.random((2,12)))
print(a)
# [[5. 0. 7. 5. 3. 7. 3. 4. 1. 4. 2. 2.]
#  [7. 2. 4. 9. 9. 7. 5. 2. 1. 9. 5. 1.]]

print(np.hsplit(a,3)) #将a三等分,a被分成了3个数组组成的列表!!!
# [array([[5., 0., 7., 5.],
#        [7., 2., 4., 9.]]), array([[3., 7., 3., 4.],
#        [9., 7., 5., 2.]]), array([[1., 4., 2., 2.],
#        [1., 9., 5., 1.]])]

print(np.hsplit(a,(3,4))) #在第3和第4列处切片数组,最终称为包含3个数组的列表
# [array([[5., 0., 7.],
#        [7., 2., 4.]]), array([[5.],
#        [9.]]), array([[3., 7., 3., 4., 1., 4., 2., 2.],
#        [9., 7., 5., 2., 1., 9., 5., 1.]])]

#vsplit会垂直方向切片,array_split会根据给定的参数来切片


