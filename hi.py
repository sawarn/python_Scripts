from PIL import Image
import cv2
import matplotlib.pyplot as plt
image = cv2.imread("C://Users//Shivam//Desktop//New folder (2)//1-1.png", 1)
stretch_near = cv2.resize(image, (1152,500)
               )
plt.imshow(stretch_near)
plt.show()
print(image.size) # Output: (1200, 776)
print(stretch_near.size) # Output: (400, 400)
