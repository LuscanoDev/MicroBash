import os

def write(nameFile):
    with open(nameFile, 'w') as f:
        f.close()

try:
    if not param == None or not param == '':
        part1 = param
        write(part1)
        print(f"File '{part1}' created with success.")
    else:
        print(f"Use: touch <filename>")
except Exception as e:
    print(f"{e}")