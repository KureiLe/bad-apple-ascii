import time
import os

files = os.listdir('ascii')

f_i = 1
f = []
for x in files:
    f.append(f_i)
    f_i += 1

for x in f:
    file = open(f'ascii/{x}.txt')
    print(file.read())
    time.sleep(0.05)
    os.system('cls')