import numpy as np
print(np.unravel_index(99,(6,7,8)))
z=np.zeros((6,7,8))
print(z)
z[(1,5,3)]=10000
print(z)