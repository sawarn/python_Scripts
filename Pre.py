import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from numba import njit
import os
import glob
from pprint import pprint
from fnmatch import fnmatch
import random

#VISUALIZATION
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
sns.set()
import cv2
from tqdm import tqdm
#MACHINELEARNING
from sklearn import svm
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.decomposition import PCA

from glob import glob
from skimage import io
from os import listdir
import pickle

import time
import copy
#from tqdm.notebook import tqdm
#tqdm().pandas();5

print('import complete')

folder_path = r"C:\Users\Shivam\Desktop\Dataset\7415_10564_bundle_archive"

main = os.path.join(folder_path,"IDC_regular_ps50_idx5")

patient_ids = os.listdir(main)
#print(patient_ids)

columns = ["patient_id",'x','y',"target","path"]
data_rows = []
i = 0
iss = 0
isss = 0

for patient_id in patient_ids:
    for c in [0,1]:
        class_path = os.path.join(main,patient_id)+'/'+str(c)+'/'
        imgs = os.listdir(class_path)


        img_paths = sorted([class_path + img + '/' for img in imgs], key=len)
        #print(img_paths)

        # Extracting Image Coordinates
        img_coords = [img.split('_',4)[2:4] for img in imgs]
        #print(img_coords)
        x_coords = [int(coords[0][1:]) for coords in img_coords]
        #print(x_coords)
        y_coords = [int(coords[1][1:]) for coords in img_coords]
        #print(y_coords)




        for (path,x,y) in zip(img_paths,x_coords,y_coords):
            values = [patient_id,x,y,c,path]
            #print(values)
            data_rows.append({k:v for (k,v) in zip(columns,values)})
# We create a new dataframe using the list of dicts that we generated above
data = pd.DataFrame(data_rows)
#print(data.head())
def get_classes_split(series):
    ratio = np.round(series.value_counts()/series.count()*100,decimals = 1)
    return ratio

groups = [df for _, df in data.groupby('patient_id')]
random.shuffle(groups)
shuffled_data = pd.concat(groups).reset_index(drop=True)

#print(get_classes_split(data['target']))
from sklearn.model_selection import train_test_split
# Set the patient ids as indices for the dataframe
shuffled_data = data.set_index('patient_id')
# Select all columns except the target column and store it in X
X = shuffled_data.loc[:, shuffled_data.columns != 'target']
# Select the target column and store it in y
y = shuffled_data['target']

# OS stands for 'Out of Sample'
X_data, OSX_df, y_data, OSy_df = train_test_split(X, y, test_size=0.1, shuffle = False)
# We split it even further and obtain the training and testing dataframes
X_train_df, X_test_df, y_train_df, y_test_df = train_test_split(X_data, y_data, test_size=0.3, shuffle = False)



# Dataframe containing cancerous images
c_df = data.loc[data.target == 1,:]
# Dataframe containing normal images
n_df = data.loc[data.target == 0,:]

fraction_c = np.round(0.7*c_df.shape[0]).astype(int)
fraction_n = np.round(0.2*n_df.shape[0]).astype(int)

rest_c_df = c_df.iloc[fraction_c:-1]
rest_n_df = n_df.iloc[fraction_n:-1]

c_df = c_df.iloc[0: fraction_c]
n_df = n_df.iloc[0: fraction_n]

nc = c_df.shape[0]
nn = n_df.shape[0]

nrc = rest_c_df.shape[0]
nrn = rest_n_df.shape[0]

total_test = nn+nc
total_train = nrn + nrc

print("Testing Data:")
print(f'percent cancerous : {round(nc/total_test*100,1)}%')
print(f'percent non-cancerous : {round(nn/total_test*100,1)}%\n')
print("Training Data:")
print(f'percent cancerous : {round(nrc/total_train*100,1)}%')
print(f'percent non-cancerous : {round(nrn/total_train*100,1)}%')


n_train_df = c_df.append(n_df, sort = True).reset_index(drop=True)
n_test_df = rest_c_df.append(rest_n_df,sort = True).reset_index(drop=True)

#print(n_train_df.head())
#print(n_test_df.head())

def shuffle_patients(frame):
    groups = [df for _, df in frame.groupby('patient_id')]
    random.shuffle(groups)
    shuffled_df = pd.concat(groups).reset_index(drop=True)
    return shuffled_df
n_train_df = shuffle_patients(n_train_df)
get_classes_split(n_train_df['target'])

import gc
from sklearn.decomposition import IncrementalPCA
def rgb_to_grayscale(img_paths, batch_size = 10000):
    # get the total number of images
    num_of_imgs = img_paths.shape[0]
    x=num_of_imgs
    print(x)
  # initialize counter that keeps track of position of image being loaded
    pos = 0
    # initialize empty array in order fill in the image values
    grid = np.zeros((x*2500, 3))


    nan_array = np.isnan(grid)
    not_nan_array = ~ nan_array
    grid = grid[not_nan_array]


    for img_path in tqdm(img_paths, total=x):
        # Read the image into a numpy array
        img = io.imread(img_path)
        # reshape the image to such that the rgb values are the columns of the matrix
        img = img.reshape(-1, 3)
        # replace the empty array with the values inside the image
        grid[pos: pos + img.shape[0],:] = img
        # update position counter
        pos += img.shape[0]

    # initialize pca to reduce rgb scale to a single dimensional scale
    ipca = IncrementalPCA(n_components=1, batch_size=batch_size)
    # fit pca object to the contents within the grid
    ipca.fit(grid)
    # delete grid to free up sum memory
    del grid
    gc.collect()

    return ipca

img_paths = n_train_df['path']

rgb_pca = rgb_to_grayscale(img_paths)

rgb_pca.explained_variance_ratio_.sum()
print(rgb_pca.explained_variance_ratio_.sum())


fig, ax = plt.subplots(1,2,figsize = (12.5,25))

ax[0].grid(False)
ax[0].set_title("Image of Tissue Pre PCA")
ax[0].imshow(img)
###########################
# Reshape image so that pca be applied on the rgb dimension
img = img.reshape(-1, 3)
# Apply PCA on image
img = rgb_pca.transform(img)
# Reshape image so that image can be shown
img = img.reshape(50,50)
############################
ax[1].grid(False)
ax[1].set_title("Image of Tissue Post PCA")
ax[1].imshow(img)
