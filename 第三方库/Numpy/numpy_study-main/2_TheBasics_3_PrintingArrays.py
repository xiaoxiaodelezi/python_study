#打印数组

#numpy将会用相似列表的方法的来展示数组，输出形式如下：
    # 最后的轴将会被从左到右打印
    # 倒数第二的轴将会从上到下打印
    # 剩下的轴也会从上到下打印，每个切片之间都会有空白行间隔

#一维数组会以行的形式打印，二维类似矩阵，三维像是矩阵的集合

import numpy as np


a=np.arange(5)
print(a)
# [0 1 2 3 4]

b=np.arange(12).reshape(3,4)
print(b)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

c=np.arange(24).reshape(2,3,4)
print(c)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
#
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]



#如果数组太大而无法打印，numpy会自动省略中间部分，只显示头尾。

print(np.arange(10000))
#[   0    1    2 ... 9997 9998 9999]

print(np.arange(10000).reshape(100,100))
# [[   0    1    2 ...   97   98   99]
#  [ 100  101  102 ...  197  198  199]
#  [ 200  201  202 ...  297  298  299]
#  ...
#  [9700 9701 9702 ... 9797 9798 9799]
#  [9800 9801 9802 ... 9897 9898 9899]
#  [9900 9901 9902 ... 9997 9998 9999]]

#需要取消省略设置，让numpy打印所有部分，可以使用set_printoption.

# np.set_printoptions(threshold=sys.maxsize)  #需要导入sys module
