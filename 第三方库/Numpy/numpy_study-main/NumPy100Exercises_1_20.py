'''
100 numpy exercises
1-20
'''

# 1. Import the numpy package under the name np (★☆☆)
import numpy as np


# 2. Print the numpy version and the configuration (★☆☆)
print(np.__version__)


# 3. Create a null vector of size 10 (★☆☆)
z=np.zeros([10])
print(z)


# 4. How to find the memory size of any array (★☆☆)
print(z.size *z.itemsize)


# 5. How to get the documentation of the numpy add function from the command line? (★☆☆)
print(np.info(np.add))


# 6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
z=np.zeros([10])
print(z)
z[4]=1
print(z)


# 7. Create a vector with values ranging from 10 to 49 (★☆☆)
z=np.arange(10,50)
print(z)


# 8. Reverse a vector (first element becomes last) (★☆☆)
'''
只能逆转最大维度那层
'''
print(z[::-1])


# 9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
z=np.arange(0,9).reshape(3,3)
print(z)


# 10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
'''
一维直接返回所有非零位置的index
多维也可以返回，但只会返回一个2个元素的元组（row和col），通过np.transpose来得出非零位置
'''
z=np.array([1,2,0,0,4,0])
nz=np.nonzero(z)
print(nz)

z=z.reshape(2,3)
print(z)
nz=np.nonzero(z)
print(nz)
print(np.transpose(nz))


# 11. Create a 3x3 identity matrix (★☆☆)
z=np.eye(3)
print(z)


# 12. Create a 3x3x3 array with random values (★☆☆)
z=np.random.random((3,3,3))
print(z)


# 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
z=np.random.random((10,10))
print(z)
zmin,zmax=z.min(),z.max()
print(zmin,zmax)


# 14. Create a random vector of size 30 and find the mean value (★☆☆)
z=np.random.random((30))
print(np.mean(z))


# 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)
z=np.ones((10,10))
z[1:-1,1:-1]=0
print(z)


# 16. How to add a border (filled with 0's) around an existing array? (★☆☆)
z=np.ones((5,5))
m=np.zeros((5,1))
z=np.hstack([m,np.hstack([z,m])])
n=np.zeros((1,7))
z=np.vstack([n,np.vstack([z,n])])
print(z)

z=np.ones((5,5))
print(np.pad(z,pad_width=1,mode="constant",constant_values=0))

z[:,[0,-1]]=0
print(z)
z[[0,-1],:]=0
print(z)


# 17. What is the result of the following expression? (★☆☆)
print(0 * np.nan)
# nan

print(np.nan == np.nan)
# False

print(np.inf > np.nan)#inf表示一个无穷大的正数
# False

print(np.nan - np.nan)
#nan

print(np.nan in set([np.nan]))
# True

print(0.3 == 3 * 0.1)
# False


# 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
'''
np.diag对象是一维还是多维有区别
一维返回一个以一维为左上到右下对角线为所给值（接受k偏差），其余位置为0
多维返回左上到右下对角线的值（接受k偏差），结果为一维
'''
z=np.diag(1+np.arange(4),k=-1)
print(z)

z=np.diag(np.array(8).reshape(3,3),k=-1)
print(z)


# 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
z=np.zeros((8,8),dtype=int)
z[1::2,::2]=1
z[::2,1::2]=1
print(z)


# 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
print(np.unravel_index(99,(6,7,8)))
