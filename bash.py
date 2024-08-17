with open(f'/bin/bash.py') as file:
    code = file.read()
    exec(code)