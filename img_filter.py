import PIL
from PIL import Image
import shutil
import os
import re
import numpy as np
import cv2
import skimage
from skimage.transform import resize
import glob
from shutil import copyfile
import os, os.path
import matplotlib.pyplot as plt

#def filterImages(path):


    # Defining images array for
    # identifying only image files
imgs = []
ex1=[]
path=r"C:\Users\Shivam\Desktop\Calc Train Dataset"
    # List of possible images extensions
    # add if you want more
valid_images = [ ".png",".PNG" ]

    # Storing all images in images array (imgs)
#for f in os.scandir(path):
    #if (re.findall("1-1.png$",files)):
    #    ex1.append(files)
    #    print(ex1)
subfolders = [ f.path for f in os.scandir(path) if (re.findall("[0-9]$",f.path)) ]

    #imgs=(re.findall("[0-9]$",f))
    #s=imgs.split(",")
    #ex1.append(glob.glob(os.path.join(*s,"*","*","*","*1-1.png")))


    #if(re.findall("[0-9]$",f)):
    #        ex1.append(f)
    #        print(ex1)
    #else:
    #    continue
#newsize(224,224)
for dir in subfolders:
        #print(dir)
        direc=glob.glob(os.path.join(dir,"*","*","1-1.png"))
        #print(direc)
        for n,image in enumerate(direc):
            pn=plt.imread(image)
            pn=resize(pn,(224,224),anti_aliasing=True)
            plt.imshow(pn,cmap='gray')
            plt.show()

            #pn=pn.resize((224,224),PIL.Image.NEAREST)
        #    pn.show()

            #pixel_array=np.asarray(pn)
            #print(pixel_array)
        #if ext.lower() not in valid_images:
            #continue
        #imgs.append(f)

    # Checking whether the filteredImages
    # directory exists or not
    #name = "filteredImages"
    #directory = os.path.join(path,name)
    #if not os.path.exists(directory):
    #    os.makedirs(directory)

    # Defining filteredIMages array for
    # storing all the images we need
    #filteredImages = []

    #for i in imgs:
    #    image = Image.open(os.path.join(path, i))

        # Storing width and height of a image
        #width, height = image.size

        # if only width exceeds the thresholdWidth
        #if (width < thresholdWidth and
        #    height < thresholdHeight):
        #    copyfile(os.path.join(path, i),
        #             os.path.join(path,name,i))

            #image.resize((thresholdWidth,
            #            (thresholdWidth * height)
            #                    // width)).save(i)

        # if only height exceeds the thresholdHeight
        #elif (width <= thresholdWidth and
              #height > thresholdHeight):

            #image.resize(((thresholdHeight * width)
                        #// height, thresholdHeight)).save(i)

        # if both the paramateres exceeds
        # the threshold attributes
        #elif (width > thresholdWidth and
        #      height > thresholdHeight):

        #    image.resize((thresholdWidth, thresholdHeight)).save(i)

        #filteredImages.append(i)

    # returning the filteredImages array
    #return filteredImages

# Driver Code
#if _name_ == '_main_':

#    filteredImages = []

    # Enter the path of the python sizeFilter
    # file, the thresholdWidth(in pixels) and
    # thresholdHeight(in pixels)
#    filteredImages = filterImages(r"D:\Cancer Diagnosis poject\new", 1000, 1000)
