import numpy as np

#简单的赋值不会创建对象的拷贝或者数据

a=np.array(
    [[0,1,2,3],
    [4,5,6,7],
    [8,9,10,11]])
b=a


c=a.view()
# 视图方法创造一个新的数组对象指向同一数据。
# 视图和源数据，数据用的同一内存，但是组织形式不同。

print(c is a)
# False
print(c.base is a)
# True

print(c.flags.owndata) #c并没有数据
# False

c=c.reshape((2,6))

print(a.shape) #对c的结构修改对a无效
# (3, 4)

c[0,4]=1234

print(a) #对c的更改对a有效
# [[   0    1    2    3]
#  [1234    5    6    7]
#  [   8    9   10   11]]
