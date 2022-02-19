import cv2
import matplotlib.pyplot as plt
img = cv2.imread('1-1.png', 1)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
heatmap_img = cv2.applyColorMap(gray_img, cv2.COLORMAP_JET)
#fin = cv2.addWeighted(heatmap_img, 0.5, frame, 0.5, 0)
plt.imshow(heatmap_img)
plt.show()
