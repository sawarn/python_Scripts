# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 18:12:26 2020

@author: Shivam
"""
import json
from flask import Flask,request,jsonify,Response
import base64
import numpy as np
import imageio
import soilNET
from matplotlib.pyplot import imshow
from keras.preprocessing import image

app = Flask(__name__)


@app.route("/",methods=["POST"])
def predict():
    data=request.get_json(force=True)
    #data_base =
    base64_img=str(data['base64'])
    file_name=data["ID"]
    with open(file_name,'wb') as f:
        f.write(base64.b64decode(base64_img+'b==='))
    image_path= file_name
    img = image.load_img(image_path, target_size=(150,150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x/255.0
    #print('Input image shape:', x.shape)
    #my_image = imageio.imread(image_path)
    #imshow(my_image)
    print("class prediction vector [Alluvial, Black, Clayey, Latterite, Red, Sandy] = ")
    prediction=soilNET.model.predict(x)
    output=prediction[0]
    return Response((output))
    

if __name__ == "__main__":
    app.run()