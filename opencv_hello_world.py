import cv2
image = cv2.imread("rabbit_green_screen.jpg")
print("width: %d pixels" % image.shape[1])
print("height: %d pixels" % image.shape[0])
print("channels: %d" % image.shape[2])
cv2.imshow("Trex Image", image)

h,w,d = image.shape

image[0:5, 0:]=(0,0,255)
image[h-5:,:]=(0,0,255)
image[0:h,0:5]=(0,0,255)
image[:,w-5:]=(0,0,255)


cv2.imshow("Trex with line image", image)

cv2.waitKey(0)
out_file_name = "trex_with_line.png"
cv2.imwrite(out_file_name, image)
