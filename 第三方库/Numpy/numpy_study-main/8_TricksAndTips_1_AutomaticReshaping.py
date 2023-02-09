#自动塑形
#在改变数组形状时，可以省略其中的一个数字，这个维度会被自动计算

import numpy as np

a=np.arange(30)
b=a.reshape((2,-1,3)) #负数被认为时省略
print(b.shape)
# (2, 5, 3)
print(b)
'''
[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]
  [ 9 10 11]
  [12 13 14]]

 [[15 16 17]
  [18 19 20]
  [21 22 23]
  [24 25 26]
  [27 28 29]]]

'''
