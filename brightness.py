import cv2

image = cv2.imread("rabbit_green_screen.jpg")

image = image*1.25


cv2.imshow("rabbit", image)
