#	Numpy

##	1.Prerequistes



## 2.TheBasics

```python
np.arrange()

ndarray.reshape()

ndarray.dtype()

np.array()

np.zero()

np.ones()

np.empty()

ndarray_a-ndaary_b #对应位置相减

ndarray**2	#所有位置**2

np.sin() #所有位置取sin

ndarray < 35 #判断所有位置并返回每个位置的布尔值

ndarray_a * Ndarray_b #所有位置对应值相乘

ndarray_a @ ndarray_b #矩阵相乘  
ndarray_a.dot(ndarray_b) #同上

#+=等二元运算符会更改原始数据

rg=np.random.default_rng(给定值) #返回一个0-给定值的随机范围的rg
rg.random()#使用rg来初始化一个随机元素的ndarray

#a+=b不一定可以，a+b必须是和a一致的数据类型才成功，不然报错

np.linspace(start,end,number)#均匀间隔number个start和end之间的元素（包含start和end）

np.exp()#返回以e为底的给定list元素的次方的ndarray

ndarray.sum()
ndarray.min()
ndarray.max()
ndarray.cumsum() #元素前加上元素自己的累加
#参数中可以给定axis，0表示每列，1表示行

np.sqrt()
np.add(ndarray_a,ndarray_b)


#ndarray 可以被索引、切片和迭代
np.fromfunction(f,f需要的参数元组,dtype)#用f的方式初始化一个元组，其中x，y是shape，作为f的参数，f的返回值为ndarray在x，y位置的值

#ndarray[横切,竖切]，参数不足时等同于:，...类似python的接受值*功能

ndarray.flat#以ndarray在内存中的数据顺序作为迭代顺序的迭代器

```



## 3.Shape Manipulation

```python
np.floor() #floor和ceil在负数时是正数的取负数操作，这个要注意

ndarray.ravel() #将所有元素压扁成为一个一维数组

ndarray.reshape() #变换改变各个维度和维度中的元素，ndarray不会改变

ndarray.T #转置，ndarray不会改变

ndarray.resize() #改变各个维度和维度中的元素，ndarray会改变

np.vstack(ndarray_1,ndarray_2)  #垂直拼接
np.hstack(ndarray_1,ndarray_2)  #竖向拼接
np.colum_stack(ndarray_1,ndarray_2) #两个都是一维的，会变成一个二维的ndarray。如果都是二维，则等同于hstack

#np.row_stack等于np.vstack
#np.column_stack不一定等于np.hstack

#理解的不好
np.newaxis 
a[:,np.newaxis] #将a看成一个一维元素，并转置（从一行变为一列）本质是增加了一个维度，那么原来的a就是这个维度中的

np.hsplit(ndarray,参数) #如果参数是一个元素或者只包含一个元素的元组，那么ndarray会被等分切割成一个list，里面包含元素值的个数的ndarray。如果参数是一个多个元素的元组，那么会在各个元素的位置切片，返回一个list，包含各个ndarray
np.vsplit(ndarray,参数)#类似hsplit

```



##	4.Copies and Views

###	4.1 Not Copy at All

```python
import numpys as np

#b=a赋值操作只是引用传递，指向同一个地址
a=np.array(
    [[0,1,2,3],
    [4,5,6,7],
    [8,9,10,11]])
b=a
print(b is a )
```

### 4.2 View or Shadow Copy

```python
c=a.view()
# view返回的也是ndarray
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

'''
总结：
c作为a的view不等于a，但是c.base等于a。
c自己没有数据，c的底层数据是a
改变c的维度不会影响a的维度
改变c的值会影响a的值
view可以看成是a的浅拷贝
'''
```

### 4.3 Deep Copy

```python
a=np.array(
    [[0,1,2,3],
    [4,5,6,7],
    [8,9,10,11]])

d=a.copy()#深拷贝，d与a没有任何关系

print(d is a) #d和a本质上无关
# False
print(d.base is a)
# False


d[0,0]=9999 #对d的修改不影响a
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# 有时候会在切片后调用复制,如果原数组不再被需要的话.比如,a是一个很大的中间处理环节的结果,而最为最终结果的b只是a的很小一部分,
# 那么就会在切片创建b时应该使用深复制

a=np.arange(int(1e8))
b=a[:100].copy()
del a
print(b)
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
#  24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
#  48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
#  72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95
#  96 97 98 99]
```

### 4.4 Functions and Methods

一些numpy的基础函数

Array Creation

[`arange`](https://numpy.org/devdocs/reference/generated/numpy.arange.html#numpy.arange), [`array`](https://numpy.org/devdocs/reference/generated/numpy.array.html#numpy.array), [`copy`](https://numpy.org/devdocs/reference/generated/numpy.copy.html#numpy.copy), [`empty`](https://numpy.org/devdocs/reference/generated/numpy.empty.html#numpy.empty), [`empty_like`](https://numpy.org/devdocs/reference/generated/numpy.empty_like.html#numpy.empty_like), [`eye`](https://numpy.org/devdocs/reference/generated/numpy.eye.html#numpy.eye), [`fromfile`](https://numpy.org/devdocs/reference/generated/numpy.fromfile.html#numpy.fromfile), [`fromfunction`](https://numpy.org/devdocs/reference/generated/numpy.fromfunction.html#numpy.fromfunction), [`identity`](https://numpy.org/devdocs/reference/generated/numpy.identity.html#numpy.identity), [`linspace`](https://numpy.org/devdocs/reference/generated/numpy.linspace.html#numpy.linspace), [`logspace`](https://numpy.org/devdocs/reference/generated/numpy.logspace.html#numpy.logspace), [`mgrid`](https://numpy.org/devdocs/reference/generated/numpy.mgrid.html#numpy.mgrid), [`ogrid`](https://numpy.org/devdocs/reference/generated/numpy.ogrid.html#numpy.ogrid), [`ones`](https://numpy.org/devdocs/reference/generated/numpy.ones.html#numpy.ones), [`ones_like`](https://numpy.org/devdocs/reference/generated/numpy.ones_like.html#numpy.ones_like), [`r_`](https://numpy.org/devdocs/reference/generated/numpy.r_.html#numpy.r_), [`zeros`](https://numpy.org/devdocs/reference/generated/numpy.zeros.html#numpy.zeros), [`zeros_like`](https://numpy.org/devdocs/reference/generated/numpy.zeros_like.html#numpy.zeros_like)

Conversions

[`ndarray.astype`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.astype.html#numpy.ndarray.astype), [`atleast_1d`](https://numpy.org/devdocs/reference/generated/numpy.atleast_1d.html#numpy.atleast_1d), [`atleast_2d`](https://numpy.org/devdocs/reference/generated/numpy.atleast_2d.html#numpy.atleast_2d), [`atleast_3d`](https://numpy.org/devdocs/reference/generated/numpy.atleast_3d.html#numpy.atleast_3d), [`mat`](https://numpy.org/devdocs/reference/generated/numpy.mat.html#numpy.mat)

Manipulations

[`array_split`](https://numpy.org/devdocs/reference/generated/numpy.array_split.html#numpy.array_split), [`column_stack`](https://numpy.org/devdocs/reference/generated/numpy.column_stack.html#numpy.column_stack), [`concatenate`](https://numpy.org/devdocs/reference/generated/numpy.concatenate.html#numpy.concatenate), [`diagonal`](https://numpy.org/devdocs/reference/generated/numpy.diagonal.html#numpy.diagonal), [`dsplit`](https://numpy.org/devdocs/reference/generated/numpy.dsplit.html#numpy.dsplit), [`dstack`](https://numpy.org/devdocs/reference/generated/numpy.dstack.html#numpy.dstack), [`hsplit`](https://numpy.org/devdocs/reference/generated/numpy.hsplit.html#numpy.hsplit), [`hstack`](https://numpy.org/devdocs/reference/generated/numpy.hstack.html#numpy.hstack), [`ndarray.item`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.item.html#numpy.ndarray.item), [`newaxis`](https://numpy.org/devdocs/reference/constants.html#numpy.newaxis), [`ravel`](https://numpy.org/devdocs/reference/generated/numpy.ravel.html#numpy.ravel), [`repeat`](https://numpy.org/devdocs/reference/generated/numpy.repeat.html#numpy.repeat), [`reshape`](https://numpy.org/devdocs/reference/generated/numpy.reshape.html#numpy.reshape), [`resize`](https://numpy.org/devdocs/reference/generated/numpy.resize.html#numpy.resize), [`squeeze`](https://numpy.org/devdocs/reference/generated/numpy.squeeze.html#numpy.squeeze), [`swapaxes`](https://numpy.org/devdocs/reference/generated/numpy.swapaxes.html#numpy.swapaxes), [`take`](https://numpy.org/devdocs/reference/generated/numpy.take.html#numpy.take), [`transpose`](https://numpy.org/devdocs/reference/generated/numpy.transpose.html#numpy.transpose), [`vsplit`](https://numpy.org/devdocs/reference/generated/numpy.vsplit.html#numpy.vsplit), [`vstack`](https://numpy.org/devdocs/reference/generated/numpy.vstack.html#numpy.vstack)

Questions

[`all`](https://numpy.org/devdocs/reference/generated/numpy.all.html#numpy.all), [`any`](https://numpy.org/devdocs/reference/generated/numpy.any.html#numpy.any), [`nonzero`](https://numpy.org/devdocs/reference/generated/numpy.nonzero.html#numpy.nonzero), [`where`](https://numpy.org/devdocs/reference/generated/numpy.where.html#numpy.where)

Ordering

[`argmax`](https://numpy.org/devdocs/reference/generated/numpy.argmax.html#numpy.argmax), [`argmin`](https://numpy.org/devdocs/reference/generated/numpy.argmin.html#numpy.argmin), [`argsort`](https://numpy.org/devdocs/reference/generated/numpy.argsort.html#numpy.argsort), [`max`](https://docs.python.org/3/library/functions.html#max), [`min`](https://docs.python.org/3/library/functions.html#min), [`ptp`](https://numpy.org/devdocs/reference/generated/numpy.ptp.html#numpy.ptp), [`searchsorted`](https://numpy.org/devdocs/reference/generated/numpy.searchsorted.html#numpy.searchsorted), [`sort`](https://numpy.org/devdocs/reference/generated/numpy.sort.html#numpy.sort)

Operations

[`choose`](https://numpy.org/devdocs/reference/generated/numpy.choose.html#numpy.choose), [`compress`](https://numpy.org/devdocs/reference/generated/numpy.compress.html#numpy.compress), [`cumprod`](https://numpy.org/devdocs/reference/generated/numpy.cumprod.html#numpy.cumprod), [`cumsum`](https://numpy.org/devdocs/reference/generated/numpy.cumsum.html#numpy.cumsum), [`inner`](https://numpy.org/devdocs/reference/generated/numpy.inner.html#numpy.inner), [`ndarray.fill`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.fill.html#numpy.ndarray.fill), [`imag`](https://numpy.org/devdocs/reference/generated/numpy.imag.html#numpy.imag), [`prod`](https://numpy.org/devdocs/reference/generated/numpy.prod.html#numpy.prod), [`put`](https://numpy.org/devdocs/reference/generated/numpy.put.html#numpy.put), [`putmask`](https://numpy.org/devdocs/reference/generated/numpy.putmask.html#numpy.putmask), [`real`](https://numpy.org/devdocs/reference/generated/numpy.real.html#numpy.real), [`sum`](https://numpy.org/devdocs/reference/generated/numpy.sum.html#numpy.sum)

Basic Statistics

[`cov`](https://numpy.org/devdocs/reference/generated/numpy.cov.html#numpy.cov), [`mean`](https://numpy.org/devdocs/reference/generated/numpy.mean.html#numpy.mean), [`std`](https://numpy.org/devdocs/reference/generated/numpy.std.html#numpy.std), [`var`](https://numpy.org/devdocs/reference/generated/numpy.var.html#numpy.var)

Basic Linear Algebra

[`cross`](https://numpy.org/devdocs/reference/generated/numpy.cross.html#numpy.cross), [`dot`](https://numpy.org/devdocs/reference/generated/numpy.dot.html#numpy.dot), [`outer`](https://numpy.org/devdocs/reference/generated/numpy.outer.html#numpy.outer), [`linalg.svd`](https://numpy.org/devdocs/reference/generated/numpy.linalg.svd.html#numpy.linalg.svd), [`vdot`](https://numpy.org/devdocs/reference/generated/numpy.vdot.html#numpy.vdot)



## 5.Less Basic

### 广播原则

广播原则允许全局函数通过一个方法来处理形状不同的输入。

原则第一条，如果所有输入的数组没有相同的维度，会重复前置“1”来填充较小的数组直到所有的数组都有相同的维度。

原则第二条保证了一个只有1维的那个特别维度将会被拓展成和最大的维度一致，所有值会假定和那个拓展的部分一样。

经过这样的拓展，所有的数组都可以完全匹配。

更多细节请查看 [Broadcasting](https://numpy.org/devdocs/user/basics.broadcasting.html#basics-broadcasting).

示例1：

```python
import numpy as np

a=np.ones((2,3))
b=np.arange(3)
print(a.shape)
print(b.shape)

print(a)
print(b)
print(a+b)

'''
(2, 3)
(3,)
[[1. 1. 1.]
 [1. 1. 1.]]
[0 1 2]
[[1. 2. 3.]
 [1. 2. 3.]]
'''
```

示例2：

```python
import numpy as np

a=np.arange(3).reshape(3,1)
b=np.arange(3)
print(a.shape)
print(b.shape)

print(a)
print(b)
print(a+b)

'''
结果
(3, 1)
(3,)
[[0]
 [1]
 [2]]
[0 1 2]
[[0 1 2]
 [1 2 3]
 [2 3 4]]
'''


'''
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
012
123
234
'''
```



## 6. Advanced indexing and index tricks

### 6.1 Indexing with Arrays of Indices

```python
#索引进阶和索引技巧

#numpy可以提供比python序列更多的索引工具。
#除了以整数和切片方式索引，如我们所见，数组可以通过整数数组和布尔数组索引。

import numpy as np

#ndarray可以直接运算，运算会作用于所有元素
a=np.arange(12)**2
print(a)
# [  0   1   4   9  16  25  36  49  64  81 100 121]

i=np.array([1,1,3,8,5])
print(a[i]) #通过数组参数索引
# [ 1  1  9 64 25]

#注意这里j也是一个ndarray
#a[ndarray]将会将a的元素按照j的排列方式返回，其中的值为a的对应j值
j=np.array([[3,4],[9,7]])
print(a[j]) #a的元素按照j数组方式排列，值为a中索引值为j的数值
# [[ 9 16]
#  [81 49]]

#当被索引的数组是个多维数组，单个的索引数组关联到a的第一个维度。下面的例子是一个关于如何使用调色板将
#一张图片标签转为一张彩色图片

palette=np.array([
    [0,0,0],    #black
    [255,0,0],  #red
    [0,255,0],  #green
    [0,0,255],  #blue
    [255,255,255]   #white
])

#单个索引关联到palette的第一维度，也就是列
image=np.array([
    [0,1,2,0],
    [0,3,4,0]
])
print(palette[image])   #(2,3,4)彩色画面
# [[[  0   0   0]   #palette[0]
#   [255   0   0]   #palette[1]
#   [  0 255   0]   #palette[2]
#   [  0   0   0]]  #palette[0]
#
#  [[  0   0   0]   #palette[0]
#   [  0   0 255]   #palette[3]
#   [255 255 255]   #palette[4]
#   [  0   0   0]]] #palette[0]


#我们可以索引超过一个维度。对每个维度的索引数组必须有相同的形状。
#i和j的相同位置组成a索引值，然后放在对应的位置
a=np.arange(12).reshape(3,4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

i = np.array([   #a的第一个维度
    [0,1],
    [1,2]
])

j=np.array([    #a的第二个维度
    [2,1],
    [3,3]
])

print(a[i,j]) #i和j必须拥有相同的形状
# [[ 2  5]   #a[i00 j00] a[i01 j01]
#  [ 7 11]]  #a[i10 j10] a[i11 j11]

print(a[i,2])
# [[ 2  6]
#  [ 6 10]]

print(a[:,j])  #a是（3，4），第一个切片，表示a第一个维度的每个元素，也就是3个，j表示对每个第一维度的元素去j索引的值
# [[[ 2  1]
#   [ 3  3]]
#
#  [[ 6  5]
#   [ 7  7]]
#
#  [[10  9]
#   [11 11]]]


#在python中，arr[i,j]和arr[(i,j)]含义完全一致，所以在numpy中，我们可以给i和j赋值一个元组，然后做索引
l=(i,j)
print(a[l]) #意义和a[i,j]一致
# [[ 2  5]
#  [ 7 11]]


#但是我们不能把i和j存入一个数组，因为这个数组会被解释为对于a的第一个维度的索引
s=np.array([i,j])
# print(a[s])
# Traceback (most recent call last):
#   File "D:/Study/Python/numpy/test.py", line 94, in <module>
#     print(a[s])
# IndexError: index 3 is out of bounds for axis 0 with size 3



print(a[tuple(s)]) #可以把s元组化，然后作为a的索引参数
# [[ 2  5]
#  [ 7 11]]


#另一个常用的利用数组作为索引条件的是寻找时间相关的最大值

time=np.linspace(20,145,5)  #时间刻度
data=np.sin(np.arange(20)).reshape(5,4)  #4个时间相关的系列
print(time)
# [ 20.    51.25  82.5  113.75 145.  ]
print(data)
# [[ 0.          0.84147098  0.90929743  0.14112001]
#  [-0.7568025  -0.95892427 -0.2794155   0.6569866 ]
#  [ 0.98935825  0.41211849 -0.54402111 -0.99999021]
#  [-0.53657292  0.42016704  0.99060736  0.65028784]
#  [-0.28790332 -0.96139749 -0.75098725  0.14987721]]

ind=data.argmax(axis=0) #axis=0 表示垂直方向
print(ind)
# [2 0 3 1]

time_max=time[ind]
print(time_max)
# [ 82.5   20.   113.75  51.25]

data_max=data[ind,range(data.shape[1])]  #本质是data然后[数组1，数组2]的切片
print(data_max)
# [0.98935825 0.84147098 0.99060736 0.6569866 ]

print(np.all(data_max==data.max(axis=0)))
# True


#你也可以用一个索引数组作为目标
a=np.arange(5)
print(a)
# [0 1 2 3 4]
a[[1,3,4]]=0 #用一个列表作为索引，a的所有列表中的索引值都赋值0
print(a)
# [0 0 2 0 0]


#但是当索引列表中的数据有重复，指定值会多次计算，并留下最终值

a=np.arange(5)
print(a)
# [0 1 2 3 4]
a[[0,0,2]]=[1,2,3]
print(a) #a0被赋值两次，1和2，最终值为2
# [2 1 3 3 4]

#
#这是合理的，但是当你使用python下的+=时，输出结果可能不是预期的
a=np.arange(5)
a[[0,0,2]]+=1 #在这里+=只会被计算一次，特别需要注意
print(a)
# [1 1 3 3 4]
#虽然a0被调用2次，但是只被加了1此，这是由于python要求a+=1 等于a=a+1

```

###	6.2 Indexing with Boolean Arrays

```python
#我们可以使用索引数组包含数组或者整数来索引我们提供的数据，使用布尔索引的提取方式不同。
#我们只是选择是否需要这个数据

# 最自然的方式是使用和原数组一样的布尔数组

import numpy as np
import matplotlib

#ndarray 可以直接通过比较运算符返回bool
a=np.arange(12).reshape(3,4)
b=a>4
print(b)
# [[False False False False]
#  [False  True  True  True]
#  [ True  True  True  True]]

# a[b]返回一个所有值都为True的一维
print(a[b])
# [ 5  6  7  8  9 10 11]

#这个方法非常有用
a[b]=0 #选择所有大于4的数，然后重置为0
print(a)
# [[0 1 2 3]
#  [4 0 0 0]
#  [0 0 0 0]]

#一个布尔索引创建图片的例子

import matplotlib.pyplot as plt
def mandelbrot(h, w, maxit=20):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    #注意np.orgid的参数
    y, x = np.ogrid[-1.4:1.4:h*1j, -2:0.8:w*1j]
    c = x + y * 1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + c
        diverge = z * np.conj(z) > 2**2       # who is diverging
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i                    # note when
        z[diverge] = 2                          # avoid diverging too much

    return divtime
plt.imshow(mandelbrot(400, 400))
plt.show()

#第二种布尔索引方法和整数索引更加类似，对于数组上每一个维度，我们给于一个1维的布尔数组。

a=np.arange(12).reshape(3,4)
print(a)
b1=np.array([False,True,True])
b2=np.array([True,False,True,False])

print(a[b1,:]) #第0行false没有被选入
# [[ 4  5  6  7]
#  [ 8  9 10 11]]

print(a[:,b2]) #第0列和第2列被选中
# [[ 0  2]
#  [ 4  6]
#  [ 8 10]]

print(a[b1,b2])
# [ 4 10]

#需要注意的是1维的布尔数组长度必须符合原数组参与切片的维度的长度。b1长度为3，b2长度为4.

```

### 6.3 The ix_() function

`ix_`函数可用于组合不同的向量以获得每个 n-uplet 的结果。例如，如果要计算从向量 a、b 和 c 中的每一个中提取的所有三元组的所有 a+b*c：

```python
#ix_()函数

import numpy as np

a=np.array([2,3,4,5])
b=np.array([8,5,4])
c=np.array([5,4,6,8,3])
ax,bx,cx=np.ix_(a,b,c)
print(ax) #a被转换为一个(4,1,1)
# [[[2]]
#
#  [[3]]
#
#  [[4]]
#
#  [[5]]]
print(ax.shape) #b
# (4, 1, 1)

print(bx) #b被转换为一个(1,2,1) 因为b作为ix_的第二个参数
# [[[8]
#   [5]
#   [4]]]
print(bx.shape)
# (1, 3, 1)

print(cx)#c被转换为一个(1,1,5) 因为c作为ix_的最后一个参数
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


```

可以这样设置reduce

```python
def ufunc_reduce(ufct,*vectors):
    vs=np.ix_(*vectors)
    r=ufct.identity
    for v in vs:
        r=ufct(r,v)
    return r
```

然后这样使用它

```python
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

```

## 7.LinearAlgebra：SimpleArrayOperation

```python
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

```



## 8. Tricks and Tips

### 8.1 “Automatic” Reshaping

在改变数组形状时，可以省略其中的一个数字，这个维度会被自动计算

```python
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

```



### 8.2 向量叠加

在numpy中通过 `column_stack`, `dstack`, `hstack` and `vstack` 函数来进行向量叠加。选择什么样的函数取决于你需要在哪个维度上叠加。 

```python
import numpy as np

x=np.arange(0,10,2)
y=np.arange(5)

m=np.vstack([x,y])
print(m)
# [[0 2 4 6 8]
#  [0 1 2 3 4]]

xy=np.hstack([x,y])
print(xy)
# [0 2 4 6 8 0 1 2 3 4]
```



### 8.3 直方图

```python
import numpy as np

rg=np.random.default_rng(1)

import matplotlib.pyplot as plt

mu,sigma = 2, 0.5

v=rg.normal(mu,sigma,10000)#高斯分布

plt.hist(v,bins=50,density=1)

(n,bins)=np.histogram(v,bins=50,density=True)

plt.plot(.5*(bins[1:]+bins[:-1]),n)

plt.show()
```



