import os

def remove_frames():
    files = os.listdir('frames')
    for x in files:
        os.remove(f'frames/{x}')
        print(f'{x} has been removed')

def remove_ascii():
    files = os.listdir('ascii')
    for x in files:
        os.remove(f'ascii/{x}')
        print(f'{x} has been removed')

remove_ascii()