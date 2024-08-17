with open(configFile, 'r') as file:
    lines = file.readlines()

name = input('What username do you want? ')
username = name
            
lines[1] = f"username = '{name}'\n"

with open(configFile, 'w') as f:
    for line in lines:
        f.write(line)