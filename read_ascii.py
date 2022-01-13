import time
import os
import shutil

columns = shutil.get_terminal_size().columns

files = os.listdir('ascii')

f_i = 1
f = []
for x in files:
    f.append(f_i)
    f_i += 1

os.system('cls')

for x in f:
    file = open(f'ascii/{x}.txt')
    print(file.read().center(columns), end='\r')
    time.sleep(1/40)