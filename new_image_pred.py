# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:27:11 2020

@author: Rashi
"""
import os
import imageio
#import scipy.misc
from matplotlib.pyplot import imshow
#from cancer import train_model 
from keras.preprocessing import image
import numpy as np
import soilNET
from tensorflow.keras.optimizers import Adagrad
from keras.models import model_from_json

# initialize our number of epochs, initial learning rate, and batch
# size
NUM_EPOCHS = 40
INIT_LR = 1e-2
BS = 32

#model = soilNET.build(width=150, height=150, depth=3,
	#classes=2)
opt = Adagrad(lr=INIT_LR, decay=INIT_LR / NUM_EPOCHS)
#model.compile(loss="binary_crossentropy", optimizer=opt,
	#metrics=["accuracy"])

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("weights.h5")
print("Loaded model from disk")

loaded_model.compile(loss='binary_crossentropy', optimizer=opt,
                     metrics=['accuracy'])


imgs_path = r"C:\Users\Shivam\Desktop\Alluvial1"
img_path = os.listdir(imgs_path)
for imgs in img_path:
    i = os.path.join(imgs_path,imgs)
    img = image.load_img(i, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x/255.0
    print('Input image shape:', x.shape)
    my_image = imageio.imread(i)
    imshow(my_image)
    print("class prediction vector [p(0), p(1), p(2), p(3), p(4), p(5)  = ")
    score = loaded_model.predict(x)
    print(score)