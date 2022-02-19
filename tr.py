import pydicom as dicom
import os
import glob
import cv2
import PIL # optional
# make it True if you want in PNG format
PNG = False
# Specify the .dcm folder path
folder_path = r"C:\Users\Shivam\Desktop\test"
# Specify the output jpg/png folder path
jpg_folder_path = r"C:\Users\Shivam\Desktop\test"
i = glob('folder_path/*/*.dcm', recursive = True)
for images_path in i:
    for n, image in enumerate(images_path):
        ds = dicom.dcmread(image)
        pixel_array_numpy = ds.pixel_array
        if PNG == True:
            image = image.replace('.dcm', '.png')
        else:
            image = image.replace('.dcm', '.jpg')
            cv2.imwrite(os.path.join(jpg_folder_path, image), pixel_array_numpy)
            if n % 50 == 0:
                print('{} image converted'.format(n))
