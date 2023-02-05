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

