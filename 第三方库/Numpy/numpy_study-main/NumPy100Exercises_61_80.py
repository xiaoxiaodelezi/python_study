  
'''
Numpy 100
61-80
'''

import numpy as np


# 61. Find the nearest value from a given value in an array (★★☆)

z=np.random.uniform(0,1,10)
t=0.5
m=z.flat[np.abs(z-t).argmin()]
print(m)


# 62. Considering two arrays with shape (1,3) and (3,1), how to compute their sum using an iterator? (★★☆)
A = np.arange(3).reshape(3,1)
B = np.arange(3).reshape(1,3)
it = np.nditer([A,B,None])
for x,y,z in it: z[...] = x + y
print(it.operands[2])

# 63. Create an array class that has a name attribute (★★☆)
class NamedArray(np.ndarray):
    def __new__(cls, array, name="no name"):
        obj = np.asarray(array).view(cls)
        obj.name = name
        return obj
    def __array_finalize__(self, obj):
        if obj is None: return
        self.info = getattr(obj, 'name', "no name")

Z = NamedArray(np.arange(10), "range_10")
print (Z.name)
