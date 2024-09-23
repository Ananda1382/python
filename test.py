import os
import shutil

folders = {
    "Images": ['.jpg', '.jpeg'],
    "PDFFiles": ['.pdf']
}

orignal_location = 'C:/Users/ACHAND27/Desktop/'
Target_location = 'C:/Users/ACHAND27/Desktop/test1'

for folder in folders:
    folder_path = os.path.join(Target_location, folder)
    # if os.l