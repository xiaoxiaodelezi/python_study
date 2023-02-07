import numpy as np

a=np.arange(3).reshape(3,1)
b=np.arange(3)
print(a.shape)
print(b.shape)

print(a)
print(b)
print(a+b)

'''
012

第一步，b从(3,)变为(3,3)
b
012
012
012
第二步：a从(3,1)变为(3,3)
a
000  012
111  123
222  234

最后a+b
'''