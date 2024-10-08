# MicroBash
An easier way to use MicroPython devices

![](/imgs/img1.png)

## How to install

- Clone this repository 
- Plug your MicroPython device in your computer
- Copy the bash.py and the bin folder to your device
- Reset your device
- In python interpreter, just type  ```import bash```
  
That's it!

## Commands

- ```help``` -- display the help
- ```ls``` -- show files in current directory
- ```cd [folder]``` -- enter in a folder
- ```touch [filename]``` -- create a file
- ```rm [file]``` -- remove a file
- ```cat [file]``` -- show content from a file
- ```mkdir [folder name]``` -- create a folder
- ```rename [original file name] [new file name]``` -- rename a file to other name
- ```cowsay [message]``` -- the cow says [insert something cool here]!!
- ```web [url]``` -- request something over network and prints the response
- ```wlan [wifi name] [wifi password]``` -- connect to some wifi
- ```infofetch``` -- show some infos from your device
- ```setname``` -- set a name to your bash 'account'
- ```python [file]``` -- execute a python file
- ```size [file]``` -- see the size of a file in kilobytes

  If you want to create some command, just create a script and put in the bin folder.
