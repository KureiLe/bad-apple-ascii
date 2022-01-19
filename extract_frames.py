import cv2
import os

try:
    os.mkdir("./frames")
except OSError:
    print("Couldn't create 'frames' folder in %s ", os.getcwd())

video_name = 'video.mp4'
capture_frame_every = 1

video = cv2.VideoCapture(video_name)
frame, image = video.read()

count = 1
while frame:
    if count % capture_frame_every == 0:
        count_2 = int(count / capture_frame_every)
        cv2.imwrite(f'frames/{count_2}.png', image)
    frame, image = video.read()
    print('reading frames: ', frame)
    count += 1