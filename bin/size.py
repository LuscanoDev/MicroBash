import os

def getSize(file, kborbytes):
    params = os.stat(file)
    size = params[6]
    if kborbytes == 'kb':
        finalsize = size / 1000 
    elif kborbytes == 'b':
        finalsize = size 
    return finalsize

file = param
try:
    size = getSize(file, 'kb')
    print(f'{size}kb')
except Exception as e:
    print(f"File '{file}' not found. {e}")
