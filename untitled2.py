#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 22:33:34 2020

@author: shivam
"""
import imageio
#import scipy.misc
from matplotlib.pyplot import imshow
import soilNET
#import data_receive
import json
from keras.preprocessing import image
import numpy as np
import base64
import requests
#from requests.exceptions import HTTPErro
img_path = r"/home/shivam/Downloads/Alluvial2.jpg"
img = image.load_img(img_path, target_size=(150,150))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = x/255.0
print('Input image shape:', x.shape)
my_image = imageio.imread(img_path)
imshow(my_image)
print("class prediction vector [Alluvial, Black, Clayey, Latterite, Red, Sandy] = ")
prediction=soilNET.model.predict(x)
prediction=prediction.tolist()
output=json.dumps(prediction)
print(output)


