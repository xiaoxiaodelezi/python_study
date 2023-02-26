import numpy as np
z = np.arange(9).reshape(3,3)
for index, value in np.ndenumerate(z):
    print(index, value)
for index in np.ndindex(z.shape):
    print(index, z[index])