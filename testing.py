import numpy as np

mosaic = np.empty((4, 3, 4, 4,))
mosaic2 = mosaic.reshape(2, 2, 3, 4, 4)
print(mosaic)
print(mosaic.shape)
print(mosaic2)