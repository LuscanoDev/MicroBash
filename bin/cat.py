def read(file):
    with open(file) as f:
        data = f.read()
    return data

nameFile = param
try:
    content = read(nameFile)
    print(content)
except Exception as e:
    print(f"File '{nameFile}' not found. {e}")