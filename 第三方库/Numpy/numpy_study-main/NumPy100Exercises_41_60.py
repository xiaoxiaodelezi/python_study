'''
Numpy 100
41-60
'''

import numpy as np

# 41. How to sum a small array faster than np.sum? (★★☆)
z=np.arange(12)
print(z)
print(np.add.reduce(z))
print(np.sum(z))


# 42. Consider two random array A and B, check if they are equal (★★☆)
a = np.random.randint(0,2,5)
b = np.random.randint(0,2,5)
equal=np.allclose(a,b) #allclose 可以有参数设定差数
print(equal)

equal=np.array_equal(a,b)#完全一致，没有参数
print(equal)


# 43. Make an array immutable (read-only) (★★☆)
Z=np.zeros(10)
Z.flags.writeable=False
#Z[0]=1  #ValueError: assignment destination is read-only


# 44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)
z=np.random.random((10,2))
print(z)
x,y=z[:,0],z[:,1]
print(x)
print(y)
r=np.sqrt(x**2+y**2)
t=np.arctan2(y,x)
print(r)
print(t)


# 45. Create random vector of size 10 and replace the maximum value by 0 (★★☆)
z=np.random.random(10)
z[z.argmax()]=0
print(z)


# 46. Create a structured array with x and y coordinates covering the [0,1]x[0,1] area (★★☆)
z = np.zeros((3,5), [('x',float),('y',float)]) #y行x列
print(z)
z['x'], z['y'] = np.meshgrid(np.linspace(0,1,5),
                             np.linspace(0,1,3))
print(z)


# 47. Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj))
x=np.arange(8)
y=x+0.5
print(np.subtract.outer(x,y))
c = 1.0 / np.subtract.outer(x,y)
print(c)


# 48. Print the minimum and maximum representable value for each numpy scalar type (★★☆)
for dtype in [np.int8,np.int32,np.int64]:
    print(np.iinfo(dtype).min)
    print(np.iinfo(dtype).max)
for dtype in [np.float32, np.float64]:
    print(np.finfo(dtype).min)
    print(np.finfo(dtype).max)
    print(np.finfo(dtype).eps)


# 49. How to print all the values of an array? (★★☆)
np.set_printoptions(threshold=float("inf"))
z=np.zeros((16,16))
print(z)


#50. How to find the closest value (to a given scalar) in a vector? (★★☆)
z=np.arange(100)
v=np.random.uniform(0,100)
index=(np.abs(z-v)).argmin()
print(z[index])


# 51. Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆)
z = np.zeros(10, [ ('position', [ ('x', float),
                                  ('y', float)]),
                   ('color',    [ ('r', float),
                                  ('g', float),
                                  ('b', float)])])
print(z)


# 52. Consider a random vector with shape (100,2) representing coordinates, find point by point distances (★★☆)
z=np.random.randint(1,11,(10,2))
x,y=np.atleast_2d(z[:,0],z[:,1])
d=np.sqrt((x-x.T)**2+(y-y.T)**2)
print(d)


#53. How to convert a float (32 bits) array into an integer (32 bits) in place?
z=((np.random.rand(10)*100).astype(np.float32))
y=z.view(np.int32)
y[:]=z
print(y)



# 54. How to read the following file? (★★☆)
# 1, 2, 3, 4, 5
# 6,  ,  , 7, 8
#  ,  , 9,10,11

from io import StringIO
s=StringIO('''
1, 2, 3, 4, 5
6,  ,  , 7, 8
 ,  , 9,10,11
''')
z=np.genfromtxt(s,delimiter=",",dtype=int)
print(z)


# 55. What is the equivalent of enumerate for numpy arrays? (★★☆)
z = np.arange(9).reshape(3,3)
for index, value in np.ndenumerate(z):
    print(index, value)
for index in np.ndindex(z.shape):
    print(index, z[index])


# 56. Generate a generic 2D Gaussian-like array (★★☆)
X, Y = np.meshgrid(np.linspace(-1,1,10), np.linspace(-1,1,10))
D = np.sqrt(X*X+Y*Y)
sigma, mu = 1.0, 0.0
G = np.exp(-( (D-mu)**2 / ( 2.0 * sigma**2 ) ) )
print(G)


# 57. How to randomly place p elements in a 2D array? (★★☆)
n = 10
p = 5
Z = np.zeros((n,n))
np.put(Z, np.random.choice(range(n*n), p, replace=False),1)
print(Z)


# 58. Subtract the mean of each row of a matrix (★★☆)
X = np.random.rand(5, 10)
Y = X - X.mean(axis=1, keepdims=True)
print(Y)


# 59. How to sort an array by the nth column? (★★☆)
Z = np.random.randint(0,10,(3,3))
print(Z)
print(Z[Z[:,1].argsort()])


# 60. How to tell if a given 2D array has null columns? (★★☆)
Z = np.random.randint(0,3,(3,10))
print((~Z.any(axis=0)).any())
