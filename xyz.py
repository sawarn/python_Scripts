import pydicom as dicom
from pathlib import Path
import glob
import os
import cv2
import PIL # optional
# make it True if you want in PNG format
PNG = False
# Specify the .dcm folder path
folder_path = r"C:\Users\Shivam\Desktop\test"
# Specify the output jpg/png folder path
jpg_folder_path = r"C:\Users\Shivam\Desktop\test"
images_path=[]
ba=[]
data = Path(r'C:\Users\Shivam\Desktop\test')
ab=list(data.glob('**/*.dcm'))
for i in ab:
    path = os.path.normpath(i)
    ba=path.split(os.sep)
    images_path=ba[6]
for n, image in enumerate(images_path):
    ds = dicom.dcmread(os.path.join(folder_path, image))
    pixel_array_numpy = ds.pixel_array
    if PNG == True:
        image = image.replace('.dcm', '.png')
    else:
        image = image.replace('.dcm', '.png')
    cv2.imwrite(os.path.join(jpg_folder_path, image), pixel_array_numpy)
    if n % 50 == 0:
        print('{} image converted'.format(n))
