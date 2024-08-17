import os

caminho = param

if caminho == '..':
    os.chdir('..')
else:
    try:
        os.chdir(caminho)
    except FileNotFoundError:
        print("Folder not found.")
    except Exception as e:
        print(f"An error occurred: {e}")