import os

def remove(file):
    os.remove(file)
    
nameFile = param
try:
    remove(nameFile)
    print(f"File '{nameFile}' removed with success.")
except:
    print(f"File '{nameFile}' not found.")