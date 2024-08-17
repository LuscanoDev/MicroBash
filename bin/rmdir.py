import os

def removeDir(file):
    os.rmdir(file)

try:
    nameFile = param
    removeDir(nameFile)
    print(f"Folder '{nameFile}' removed with success.")
except Exception as e:
    print(f"Folder '{nameFile}' dosent exist. {e}")