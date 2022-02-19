import os
import shutil


def create_file_list(path):
    return_list = []

    for filenames in os.walk(path):
        for file_list in filenames:
            for file_name in file_list:
                if file_name.endswith((".jpg")):
                    return_list.append(file_name)

    return return_list

folder_location = r"C:\Users\Shivam\Desktop\test"
file_list = create_file_list(folder_location)
print(file_list)
