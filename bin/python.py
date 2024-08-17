script = param
try:
    with open(script) as file:
        code = file.read()
        exec(code)
except Exception as e:
    print(f"Use: python [file to execute] {e}")