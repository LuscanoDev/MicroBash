import os

def rename(originalName, newName):
    os.rename(originalName, newName)

try:
    if not param == '' or not param2 == '':
        originalName, newName = param, param2
        #print(f'{originalName}  {newName}')
        rename(originalName, newName)
        print(f"File '{originalName}' renamed to '{newName}'.")
    else:
        print("Use: rename <old_name> <new_name>")
except Exception as e:
    print(f'{e}')