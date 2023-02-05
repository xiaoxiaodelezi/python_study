#ix_()函数

import numpy as np

a=np.array([2,3,4,5])
b=np.array([8,5,4])
c=np.array([5,4,6,8,3])
ax,bx,cx=np.ix_(a,b,c)
print(ax)
# [[[2]]
#
#  [[3]]
#
#  [[4]]
#
#  [[5]]]
print(ax.shape)
# (4, 1, 1)

print(bx)
# [[[8]
#   [5]
#   [4]]]
print(bx.shape)
# (1, 3, 1)

print(cx)
# [[[5 4 6 8 3]]]
print(cx.shape)
# (1, 1, 5)

result=ax+bx*cx
print(result) #result[i,j,k]=ai+bj*ck
# [[[42 34 50 66 26]
#   [27 22 32 42 17]
#   [22 18 26 34 14]]
#
#  [[43 35 51 67 27]
#   [28 23 33 43 18]
#   [23 19 27 35 15]]
#
#  [[44 36 52 68 28]
#   [29 24 34 44 19]
#   [24 20 28 36 16]]
#
#  [[45 37 53 69 29]
#   [30 25 35 45 20]
#   [25 21 29 37 17]]]


def ufunc_reduce(ufct,*vectors):
    vs=np.ix_(*vectors)
    r=ufct.identity
    for v in vs:
        r=ufct(r,v)
    return r

print(ufunc_reduce(np.add,a,b,c,))
# [[[15 14 16 18 13]
#   [12 11 13 15 10]
#   [11 10 12 14  9]]
#
#  [[16 15 17 19 14]
#   [13 12 14 16 11]
#   [12 11 13 15 10]]
#
#  [[17 16 18 20 15]
#   [14 13 15 17 12]
#   [13 12 14 16 11]]
#
#  [[18 17 19 21 16]
#   [15 14 16 18 13]
#   [14 13 15 17 12]]]

#这个版本比起普通的ufunc.reduce好，因为它可以通过广播原则避免创造一个参数数组来表示数量的相乘

