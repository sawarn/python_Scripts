# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 00:26:31 2020

@author: Rashi
"""
import os
import pandas as pd
Folder_path = r"/home/shivam/Downloads/soil image/All Soil"
df= pd.read_csv("/home/shivam/Desktop/Python Scripts/Soil_data.csv")
Id=df.Soil_Id
Name=df.Soil_Type
for (file,sid,sname) in zip (sorted(os.listdir(Folder_path)),Id,Name):
    dst = str(sid)+str(sname)+".jpg"
    src = os.path.join(Folder_path,file)
    os.rename(src,os.path.join(Folder_path,dst))