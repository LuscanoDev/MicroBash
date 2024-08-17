import os
import requests
import network
import sys

running = True
configFile = 'bashconfig.py'

def cowsay(message):
    print(f"""< {message} >
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\

                ||----w |
                ||     ||
""")

username = 'dummy'

try:
    with open(configFile) as file:
        code = file.read()
        exec(code)
except Exception as e:
    print(f'Config not found, creating a config file... {e}')
    with open(configFile, 'w') as file:
        file.write("cowsay('welcome!')\n")
        file.write("username = 'micropython'\n")
    
    with open(configFile) as file:
        code = file.read()
        exec(code)


while running:
    try:
        currentDirectory = os.getcwd()
        hostname = os.uname().nodename
        response = input(f'{username}@{hostname}: {currentDirectory} $ ').strip()
        param = ''
        
        if response.startswith('exit'):
            print('bye!')
            running = False

            
        elif response.startswith('cowsay '):
            message = response[7:].strip()
            try:
                cowsay(message)
            except:
                cowsay('Use: cowsay <message>')
                
        elif response.startswith('version'):
            print('Running MicroBash V0.2')
                    
        else:
            responsesplit = response.split()
            command = response.split()[0]
            if len(responsesplit) == 2:
                param = str(response.split()[1])
            if len(responsesplit) == 3:
                param = str(response.split()[1])
                param2 = str(response.split()[2])
            with open(f'/bin/{command}.py') as file:
                code = file.read()
                exec(code)
                param = ''
                param2 = ''
    except Exception as e:
        print(f'An error occurred: {e}')
