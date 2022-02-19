from skimage.color import rgb2gray
import numpy as np
import cv
import matplotlib.pyplot as plt
#%matplotlib inline
from scipy import ndimage

image = plt.imread('1.jpeg') #reading downloaded image
image.shape
plt.imshow(image)
plt.show()

# from skimage import data
# import numpy as np
# import matplotlib.pyplot as plt
# image = data.binary_blobs()
# plt.imshow(image, cmap='gray')
# plt.show()

# from skimage import data
# import numpy as np
# import matplotlib.pyplot as plt
# image = data.astronaut()
# plt.imshow(image)
# plt.show()
# from skimage import data
# import numpy as np
# import matplotlib.pyplot as plt
# from skimage import io
# image = io.imread('1.jpeg')
# plt.imshow(image)
# plt.show()