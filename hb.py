import glob
import pydicom as dicom
import os
import cv2
import PIL # optional

# make it True if you want in PNG format
PNG = True

# Specify the .dcm folder path
folder_path = r"C:\Users\Shivam\Desktop\test"

# Specify the output jpg/png folder path
jpg_folder_path = r"C:\Users\Shivam\Desktop\test"
#images_path = os.listdir(folder_path)
#print(images_path)

#images_path = []
#p = list()
#for jpgfile in glob.iglob(os.path.join(folder_path, "","","", ".dcm")):
#for jpgfile in folder_path.glob('*/*.dcm'):
    #images_path.append(jpgfile)
#print(images_path)

#images_path = []
#for jpgfile in glob.iglob(os.path.join(folder_path,"*.dcm")):
#    images_path.append(jpgfile)
#print(images_path)


images_path = []
for i in os.listdir(folder_path):
    images_path = glob.iglob(os.path.join(folder_path, ".*dcm"))
for n, image in enumerate(images_path):
    ds = dicom.dcmread(os.path.join(folder_path, image))
    pixel_array_numpy = ds.pixel_array
    if PNG == True:
        image = image.replace('.dcm', '.png')
    else:
        image = image.replace('.dcm', '.png')
    cv2.imwrite(os.path.join(jpg_folder_path, image), pixel_array_numpy)
    print('{} image converted'.format(n))
