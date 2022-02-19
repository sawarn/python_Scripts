# -*- coding: utf-8 -*-

from flask import Flask,request,jsonify
import pickle
import numpy as np
import requests
import json
app=Flask(__name__)
model=pickle.load(open('model_pickle.pickle','rb'))
@app.route('/api',methods=['POST'])
def predict():
    data=request.get_json(force=True)
    prediction=model.predict(x)
    output=prediction[0]
    return jsonify(output)
if __name__=='__main__':
    app.run(port=8080,debug=True)
    
url=''
r=requests.post(url,json('x'))
print(r.json())












"""
import socket
import base64
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('0.0.0.0', 8080))
## Send some data, this method can be called multiple times
#sock.send("Twenty-five bytes to send")
## Receive up to 4096 bytes from a peer
while True:
    X=sock.recv(10000)
    if(len(X<1)):
        break
base64_img= X.encode('utf-8')
with open('decoded.png','wb') as f:
    decoded_data=base64.decodebytes(base64_img)
    f.write(decoded_data)
## Close the socket connection, no more data transmission
sock.close()
"""