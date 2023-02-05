import numpy as np
#基础
    #numpy的核心时一个同类型的多维度数列的组合。它是一张元素表（通常是数字），所有元素都是同一的类型，
    #通过一个非负数的元组来进行索引，在numpy的维度中，这些索引被称为“轴”。

    #举个例子，3D空间中的一个点[1,2,1]有一个轴。这个轴有3个元素，我们称这个长度是3.在下面的例子中，
    #这个数列有两个轴，第一个轴的长度是2，第二个轴的长度是3.



    #numpy的数字类被称为ndarray。也有人称之为alias array（同类数列）。必须要注意numpy.array和
    #标准python数据库中的数列类并不相同，在python中array只有一个维度，而且提供的函数也比较少。更多
    #ndarry的参数如下：

        #ndarray.ndim
        #array的轴

        #ndarray.shape
        #数列的维度。这是一个展示数组每个维度中的大小的元组。对于一个一个n行和m列的矩阵，shape的反馈
        #是(n,m)。反馈的数组中的长度就是(axes轴数,ndim数轴的长度)

        # ndarray.size
        # 数列所有元素的个数

        # ndarray.dtype
        # 这是个表示数列中元素的类型。我们可以通过python的标准类型来创建和指定dtype。此外，numpy还
        # 额外提供它自己的类型。比如numpy.int32,numpy.int16,numpy.float64。

        # ndarray.itemsize
        # 每个元素的数据大小（比特）。比如，一个float64类型的数据的itemsize是8（=64/8），一个complex32
        # 的itemsize是4（32/8）。相当于ndarray.dtype.itemsize。

        # ndarray.data
        # 包含数列中现在素有元素的缓存。通常我们不会使用这个参数，因为我们将可以通过元素在数列中的索引来获取元素。


a=np.arange(15).reshape(3,5)
print(a)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]

print(a.shape)
# (3, 5)

print(a.ndim)
# 2

print(a.dtype.name) #和书中例子有区别，书中例子是int64
#int32

print(a.itemsize) #和书中列子有区别，书中例子是8，因为int64是8位
#4

print(a.size)
#15

