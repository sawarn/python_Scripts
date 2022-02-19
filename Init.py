import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from numba import njit
import os
import glob
from pprint import pprint
from fnmatch import fnmatch

#VISUALIZATION
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
sns.set()
import cv2

print('import complete')

folder_path = r"C:\Users\Shivam\Desktop\Dataset\7415_10564_bundle_archive"

main = os.path.join(folder_path,"IDC_regular_ps50_idx5",)
#print(main)


fold = []
for i in sorted(os.listdir(main)):
    fold = glob.glob(os.path.join(main,i))
    #print(fold)
"""
class_0 = []
class_1 = []

for file in fold:
    class_0 = glob.glob(os.path.join(main,"*","0"))
    #print(class_0)
    class_1 = glob.glob(os.path.join(main,"*","1"))
    #print(class_1)

    #class_0 = os.path.join(fold,"0")
    #print(class_0)


    #path = glob.glob(os.path.join(main,file))
    #path.append(path)
    #print(path)

    #for name in path:
"""








patient_ids = os.listdir(main)
#pat_list = glob.glob(os.path.join(files,))



#print(len(files))
#print(files)


#patient_ids = sorted(os.listdir(main),key=len)
#for patient_id in patient_ids:
#    continue
#for patient_id in patient_ids:
#    print(patient_id)


class_0_total = 0
class_1_total = 0
class_0_files=[]
class_1_files=[]
for patient_id in patient_ids:
    class_0_files = glob.glob(os.path.join(main,"*" ,"0"))
    class_1_files = glob.glob(os.path.join(main,"*" ,"1"))
for x in class_0_files:
    class_0_total+=len(os.listdir(x))
#print(class_0_total)
for y in class_1_files:
    class_1_total+=len(os.listdir(y))
#print(class_1_total)    #print(len(os.listdir(y)))
    #print(os.listdir(y))    #print(class_0_files)
#print(os.listdir(class_1_files))
#class_0_total = len(class_0_files)
#class_1_total = len(class_1_files)
#print(class_0_total)
#print(class_1_total)

total_images = class_0_total + class_1_total

#print(f'Number of patches in Class 0: {class_0_total}')
#print(f'Number of patches in Class 1: {class_1_total}')
#print(f'Total number of patches: {total_images}')
    #for sd in ipath:
    #    fold = os.listdir(sd)

    #    print(fold)
columns = ["patient_id",'x','y',"target","path"]
data_rows = []
i = 0
iss = 0
isss = 0

# note that we loop through the classes after looping through the
# patient ids so that we avoid splitting our data into [all class 0 then all class 1]
for patient_id in patient_ids:
    for c in [0,1]:
        class_path = glob.glob(os.path.join(main,"*",str(c)))
    for x in class_path:
        print(x)
        #for x in class_path:
        #    imgs = os.listdir(x)
            #print(imgs)


        # Extracting Image Paths
        #for img in imgs:
        #    continue
        #for z in img:
        #    imgs_path=glob.glob(os.path.join(class_path,z))
        #    print(imgs_path)

"""        # Extracting Image Coordinates
        img_coords = [img.split('_',4)[2:4] for img in imgs]
        x_coords = [int(coords[0][1:]) for coords in img_coords]
        y_coords = [int(coords[1][1:]) for coords in img_coords]

        for (path,x,y) in zip(img_paths,x_coords,y_coords):
            values = [patient_id,x,y,c,path]
            data_rows.append({k:v for (k,v) in zip(columns,values)})
# We create a new dataframe using the list of dicts that we generated above
data = pd.DataFrame(data_rows)
print(data.shape)
data.head()
"""
