import pydicom as dicom
import os
import cv2
import PIL
import glob
PNG=True
src_dir = r"C:\Users\Shivam\Desktop\test"
dst_dir = r"C:\Users\Shivam\Desktop\abc"
for image in glob.iglob(os.path.join(src_dir,"*.dcm")):
    ds = dicom.dcmread(os.path.join(src_dir, image))
    pixel_array_numpy = ds.pixel_array
    if PNG == True:
        image = image.replace('.dcm', '.png')
    else:
        image = image.replace('.dcm', '.jpg')
    cv2.imwrite(os.path.join(dst_dir), pixel_array_numpy)
    if n % 50 == 0:
        print('{} image converted'.format(n))
