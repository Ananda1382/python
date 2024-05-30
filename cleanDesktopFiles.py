import os

folder_original = 'C:/Users/ACHAND27/Desktop/'
folder_destination = 'C:/Users/ACHAND27/Desktop/CleanedUp'
pdf_folder = 'C:/Users/ACHAND27/Desktop/CleanedUp/PdfFiles'
word_folder = 'C:/Users/ACHAND27/Desktop/CleanedUp/WordFiles/'
image_folder = 'C:/Users/ACHAND27/Desktop/CleanedUp/ImageFiles/'

def create_Folder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)

def move_files(folder_original, folder_target, entry):
    create_Folder(folder_target)
    location_original = os.path.join(folder_original, entry.name)
    location_destination = os.path.join(folder_target, entry.name)
    os.rename(location_original, location_destination)

for entry in os.scandir(folder_original):
    if os.path.isfile(entry) & entry.name.endswith('.pdf'):        
        move_files(folder_original, pdf_folder, entry)        
    elif os.path.isfile(entry) & entry.name.endswith(('.doc', '.docx', '.docs')):
        move_files(folder_original, word_folder, entry)
    elif os.path.isfile(entry) & entry.name.lower().endswith(('.jpg', '.png', '.jpeg','.gif')):
        move_files(folder_original, image_folder, entry)    