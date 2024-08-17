import sys
import os
import micropython

print(f"""-----InfoFetch-----

Username (on bash): {username}
Device name: {os.uname().nodename}
Machine: {os.uname().machine}
MicroPython version: {sys.version}
Plataform: {sys.platform}

-------------------""")