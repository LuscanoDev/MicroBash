import os
import requests
import network
import sys

rodando = True
configFile = 'bashconfig.py'

def write(nameFile, content):
    with open(nameFile, 'w') as f:
        f.write(content)

def getSize(file, kborbytes):
    params = os.stat(file)
    size = params[6]
    if kborbytes == 'kb':
        finalsize = size / 1000  # byte to kilobyte
    elif kborbytes == 'b':
        finalsize = size  # in bytes
    return finalsize
    
def read(file):
    with open(file) as f:
        data = f.read()
    return data

def remove(file):
    os.remove(file)

def removeDir(file):
    os.rmdir(file)
    
def mkdir(folder):
    os.mkdir(folder)
    
def ls():
    return os.listdir()

def rename(originalName, newName):
    os.rename(originalName, newName)
    
def cowsay(message):
    print(f"""< {message} >
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\

                ||----w |
                ||     ||""")
    
def do_connect(networkName, networkPassword):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(networkName, networkPassword)
        while not wlan.isconnected():
            pass
    print('connected!')

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


while rodando:
    try:
        currentDirectory = os.getcwd()
        response = input(f'{username} {currentDirectory} $ ').strip()
        
        if response == 'ls':
            for item in ls():
                print(item)
                
        elif response.startswith('cd '):
            caminho = response[3:].strip()
            
            if caminho == '..':
                os.chdir('..')
            else:
                try:
                    os.chdir(caminho)
                except FileNotFoundError:
                    print("Folder not found.")
                except Exception as e:
                    print(f"An error occurred: {e}")
        
        elif response.startswith('touch '):
            parts = response.split(' ', 2)
            if len(parts) == 3:
                nameFile, content = parts[1], parts[2]
                write(nameFile, content)
                print(f"File '{nameFile}' created with success.")
            else:
                print("Use: touch <filename> <content>")
        
        elif response.startswith('cat '):
            nameFile = response[4:].strip()
            try:
                content = read(nameFile)
                print(content)
            except FileNotFoundError:
                print(f"File '{nameFile}' not found.")
        
        elif response.startswith('rm '):
            nameFile = response[3:].strip()
            try:
                remove(nameFile)
                print(f"File '{nameFile}' removed with success.")
            except:
                print(f"File '{nameFile}' not found.")
                
        elif response.startswith('rmdir '):
            nameFile = response[6:].strip()
            removeDir(nameFile)
            print(f"Folder '{nameFile}' removed with success.")
        
        elif response.startswith('mkdir '):
            folderName = response[6:].strip()
            try:
                mkdir(folderName)
                print(f"Folder '{folderName}' created with success.")
            except FileExistsError:
                print(f"Folder '{folderName}' already exists.")
        
        elif response.startswith('rename '):
            parts = response.split(' ', 2)
            if len(parts) == 3:
                originalName, newName = parts[1], parts[2]
                try:
                    rename(originalName, newName)
                    print(f"File '{originalName}' renamed to '{newName}'.")
                except FileNotFoundError:
                    print(f"File '{originalName}' not found.")
            else:
                print("Use: rename <nome_atual> <novo_nome>")
        
        elif response.startswith('exit'):
            print('bye!')
            rodando = False
            
        elif response.startswith('setname'):
            with open(configFile, 'r') as file:
                lines = file.readlines()
            name = input('What username do you want? ')
            username = name
            
            lines[1] = f"username = '{name}'\n"

            with open(configFile, 'w') as f:
                for line in lines:
                    f.write(line)

            
        elif response.startswith('help'):
            print("""MicroBash created by lexpdev.xyz

help -- display this
ls -- show files in current directory
cd [folder] -- enter in a folder
touch [filename] [content] -- write something in a file
rm [file] -- remove a file
cat [file] -- show content from a file
mkdir [folder name] -- create a folder
rename [original file name] [new file name] -- rename a file to other name
cowsay [message] -- the cow says [insert something cool here]!!
web [url] -- request something over network and prints the response
wlan [wifi name] [wifi password] -- connect to some wifi
infofetch -- show some infos from your device
setname -- set a name to your bash 'account'
python [file] -- execute a python file
size [file] -- see the size of a file in kilobytes

want to execute some python code at start? edit the bashconfig.py file!""")
            
        elif response.startswith('cowsay '):
            message = response[7:].strip()
            try:
                cowsay(message)
            except:
                cowsay('Use: cowsay <message>')
                
        elif response.startswith('web '):
            url = response[4:].strip()
            try:
                networkResponse = requests.get(url)
                print(networkResponse.text)
            except requests.exceptions.RequestException as e:
                print(f"Error accessing the URL: {e}")
                
        elif response.startswith('python '):
            script = response[7:].strip()
            try:
                with open(script) as file:
                    code = file.read()
                    exec(code)
            except Exception as e:
                print(f"Use: python [file to execute]")
        
        
        elif response.startswith('wlan '):
            wlanParts = response.split(' ', 2)
            if len(wlanParts) == 3:
                networkName, networkPassword = wlanParts[1], wlanParts[2]
                do_connect(networkName, networkPassword)
                
        elif response.startswith('infofetch'):
            print(f"""-----InfoFetch-----

Username (on bash): {username}
Device name: {os.uname().nodename}
Version: {os.uname().version}
Machine: {os.uname().machine}
MicroPython version: {sys.version}
Plataform: {sys.platform}

-------------------""")

        elif response.startswith('size '):
            file = response[5:].strip()
            try:
                size = getSize(file, 'kb')
                print(f'{size}kb')
            except Exception as e:
                print(f"File '{file}' not found. {e}")
                
        elif response.startswith('version'):
            print('Running MicroBash V0.1')
                    
        else:
            print("Command not found.")
    except Exception as e:
        print(f'An error occurred: {e}')
