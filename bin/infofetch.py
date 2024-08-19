import sys
import os
import micropython

fs_stats = os.statvfs('/')

block_size = fs_stats[0]
total_blocks = fs_stats[2]
free_blocks = fs_stats[3]

total_size = block_size * total_blocks
free_size = block_size * free_blocks
used_size = total_size - free_size

used_percentage = (used_size / total_size) * 100

print(f"""-----InfoFetch-----

Username (on bash): {username}
Device name: {os.uname().nodename}
Machine: {os.uname().machine}
MicroPython version: {sys.version}
Plataform: {sys.platform}
Memory (ROM): {round(used_size / 1000, 2)} Kb / {round(total_size / 1000, 2)} Kb ({round(used_percentage)}%) 

-------------------""")
