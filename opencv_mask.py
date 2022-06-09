import cv2
import numpy as np

canvas=np.zeros((300,400,3),dtype="uint8")

cv2.rectangle(canvas,(170,50),(230,250),(0,255,0),-1)

cv2.imshow("canvas", canvas)

green_mask=canvas[:,:,1]==255

print(green_mask[150,200])

green_mask=green_mask.astype(dtype="uint8")

white_canvas=np.ones((300,400,3), dtype="uint8")*255
masked_canvas=cv2.bitwise_and(white_canvas, white_canvas, mask=green_mask)

cv2.imshow("masked canvas", masked_canvas)

