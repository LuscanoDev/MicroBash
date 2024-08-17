import os

def ls():
    return os.listdir()

for item in ls():
    print(item)