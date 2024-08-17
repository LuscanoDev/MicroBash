import os

def mkdir(folder):
    os.mkdir(folder)
    

folderName = param
try:
    mkdir(folderName)
    print(f"Folder '{folderName}' created with success.")
except FileExistsError:
    print(f"Folder '{folderName}' already exists.")