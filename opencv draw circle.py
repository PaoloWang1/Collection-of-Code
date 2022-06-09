import cv2
import numpy as np


canvas = np.zeros((350,350,3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1]//2, canvas.shape[0]//2)
white = (255,255,255)

for x in range(7):
    cv2.circle(canvas, (centerX, centerY), (x+1)*25, white)

cv2.imshow("circle", canvas)
