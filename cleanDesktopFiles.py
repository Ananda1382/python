import os
import shutil

folders = {
    "ImageFiles": ['.jpg', '.png', '.jpeg','.gif'],
    "PdfFiles": ['.pdf'],
    "WordFiles": ['.doc', '.docx', '.docs'],
    "ExcelFiles": ['.xlsx']
}

folder_original = 'C:/Users/ACHAND27/Desktop/'
folder_destination = 'C:/Users/ACHAND27/Desktop/CleanedUp'

#created the folders
def create_Folder():
    for folder in folders:
        folder_path = os.path.join(folder_destination, folder)
        print("Folder path :",folder_path)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
#Move the files into corresponding folder
for file_name in os.listdir(folder_original):
    original_file_path = os.path.join(folder_original, file_name)
    if os.path.isfile(original_file_path):        
        for folder_name, extentions in folders.items():
            for extention in extentions:
                if file_name.endswith(extention):
                    destination_Sub_folder = os.path.join(folder_destination, folder_name)
                    print("original_file_path:", original_file_path, ",Destination Folder:", destination_Sub_folder)
                    create_Folder()
                    shutil.move(original_file_path, destination_Sub_folder)
                    