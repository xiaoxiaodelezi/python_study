#我们可以使用索引数组包含数组或者整数来索引我们提供的数据，使用布尔索引的提取方式不同。
#我们只是选择是否需要这个数据

# 最自然的方式是使用和原数组一样的布尔数组

import numpy as np
import matplotlib

a=np.arange(12).reshape(3,4)
b=a>4
print(b)
# [[False False False False]
#  [False  True  True  True]
#  [ True  True  True  True]]

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

#需要注意的是1为的布尔数组长度必须符合原数组参与切片的维度的长度。b1长度为3，b2长度为4.

