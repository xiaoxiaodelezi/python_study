#简单的数组操作

import numpy as np
a=np.array([[1.0,2.0],[3.0,4.0]])
print(a)
# [[1. 2.]
#  [3. 4.]]

print(a.transpose())
# [[1. 3.]
#  [2. 4.]]

print(np.linalg.inv(a)) #逆矩阵
# [[-2.   1. ]
#  [ 1.5 -0.5]]

u=np.eye(2)
print(u)
# [[1. 0.]
#  [0. 1.]]

j=np.array([[0.0,-1.0],[1.0,0.0]])#矩阵相乘
print(j@j)
# [[-1.  0.]
#  [ 0. -1.]]

print(np.trace(u))#对角线之和
# 2.0

y=np.array([[5.],[7.]]) #以矩阵方式求线性方程
print(np.linalg.solve(a,y))
# [[-3.]
#  [ 4.]]

print(np.linalg.eig(j))#特征向量
# (array([0.+1.j, 0.-1.j]), array([[0.70710678+0.j        , 0.70710678-0.j        ],
#        [0.        -0.70710678j, 0.        +0.70710678j]]))
