'''
Numpy100
21-40

'''

import numpy as np


# 21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)
z=np.tile([[0,1],[1,0]],(4,4))
print(z)


# 22. Normalize a 5x5 random matrix (★☆☆)
z=np.random.random((5,5))
normalize_z=(z-np.mean(z)/np.std(z))
print(normalize_z)


# 23. Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)
color=np.dtype([
    ("r",np.ubyte),
    ("g",np.ubyte),
    ("b",np.ubyte),
    ("a",np.ubyte)
])


# 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)
m=np.random.random((5,3))
n=np.random.random((3,2))
print(m@n)


# 25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)
z=np.arange(11)
z[(3<z)&(z<8)]*=-1
print(z)


# 26. What is the output of the following script? (★☆☆)
print(sum(range(5),-1))
# from numpy import * #如果导入，使用numpy将不在需要前缀np，因此sum被认为是np的sum，np中range从0开始，因此最后一个位数是0
# print(sum(range(5),-1))


# 27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)
z=np.arange(1,5).reshape(2,2)
print(z)
print(z**z)
print(2 << z >> 2)
print(z <- z)
print(1j*z)
print(z / 1 / 1)
# print(z<z>z) #错误


# 28. What are the result of the following expressions?
# print(np.array(0) / np.array(0))  #错误
# print(np.array(0) // np.array(0))  #错误
print(np.array([np.nan]).astype(int).astype(float)) #[-2.14748365e+09]


# 29. How to round away from zero a float array ? (★☆☆)
z=np.random.uniform(-10,+10,10)
print(z)
print(np.copysign(np.ceil(np.abs(z)),z))


# 30. How to find common values between two arrays? (★☆☆)
z1=np.random.randint(0,10,10)
z2=np.random.randint(0,10,10)
print(np.intersect1d(z1,z2))


# 31. How to ignore all numpy warnings (not recommended)? (★☆☆)
# Suicide mode on
# defaults = np.seterr(all="ignore")
# Z = np.ones(1) / 0


# 32. Is the following expressions true? (★☆☆)
print(np.sqrt(-1) == np.emath.sqrt(-1))
print(np.sqrt(-1))
print(np.emath.sqrt(-1))


# 33. How to get the dates of yesterday, today and tomorrow? (★☆☆)
yesterday = np.datetime64("today")-np.timedelta64(1)
today = np.datetime64("today")
tomorrow = np.datetime64("today")+np.timedelta64(1)
print(yesterday,today,tomorrow)


# 34. How to get all the dates corresponding to the month of July 2016? (★★☆)
z=np.arange("2016-07",'2016-08',dtype="datetime64[D]")
print(z)


# 35. How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)
a=np.ones(3)
b=np.ones(3)*2
c=np.ones(3)*3
np.add(a,b,out=b)
np.divide(a,2,out=a)
np.negative(a,out=a)
np.multiply(a,b,out=a)
print(a)


# 36. Extract the integer part of a random array of positive numbers using 4 different methods (★★☆)
z=np.random.uniform(0,10,10)
print(z)
print(z-z%1)
print(z//1)
print(z.astype(int))
print(np.trunc(z))


# 37. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)
z=np.zeros((5,5))
z+=np.arange(5)
print(z)


# 38. Consider a generator function that generates 10 integers and use it to build an array (★☆☆)
def generate():
    for x in range(10):
        yield x
z=np.fromiter(generate(),dtype=float)
print(z)


# 39. Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)
z=np.linspace(0,1,11,endpoint=False)[1:]
print(z)

print("aaa")
# 40. Create a random vector of size 10 and sort it (★★☆)
z=np.random.random(10)
z.sort()
print(z)
