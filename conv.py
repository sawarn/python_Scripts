from PIL import Image
import os
import cv
import glob
import matplotlib.pyplot as plt
imgpth=[]
pre=''
ext=''
newext='.png'
x=r"C:\Users\Shivam\Desktop\all-mias"
for i in os.listdir(x):
    if i.endswith(".pgm"):
        #imgpth=glob.glob(os.path.join(x,"*.pgm"))
        #print(i)
        pre,ext=os.path.splitext(i)
        imgpth=os.rename(i,pre+newext)
        print(imgpth)
    #if i.endswith(".pgm"):
    #    y=i
    #    Image.open()
