import PIL.Image
import os
import time

try:
    os.mkdir("./ascii")
except OSError:
    print("Couldn't create 'ascii' folder in %s ", os.getcwd())

file_list = sorted(os.listdir('frames'))

for x in file_list:
    # Load Image
    numberpng = x
    path = f'frames/{x}'
    image = PIL.Image.open(path)

    # Resize Image
    WIDTH, HEIGHT = image.size
    WIDTH_new = 100
    HEIGHT_new = WIDTH_new * HEIGHT / WIDTH
    image = image.resize((int(WIDTH_new), int(HEIGHT_new)))

    # Convert to Grayscale
    image = image.convert("L")

    # Make Ascii
    pixels = image.getdata()
    chars = [".", ".", ".", ".", ".", ".", "%", "%", "%", "%", "%"]
    ascii_str = ''
    for x in pixels:
        ascii_str += chars[x//25]

    # Split String Based on Width of Image
    ascii_str_count = len(ascii_str)
    ascii_img = ''
    for x in range(0, ascii_str_count, WIDTH_new):
        ascii_img += ascii_str[x:x+WIDTH_new] + '\n'

    # Upload
    file_list_new = str(numberpng).replace('.png', '')
    with open(f'ascii/{file_list_new}.txt', 'w') as f:
        f.write(ascii_img)
    print(f'{file_list_new}.txt done')