import cv2
import numpy as np

def sortSecond(val):
    return val[1]

# Read image
im=cv2.imread("images\\rubiks2.png")
cv2.imshow("rubik's cube", im)

im_bw=cv2.imread("images\\rubiks2.png", cv2.IMREAD_GRAYSCALE)
#im=cv2.imread("images\\blob.jpg", cv2.IMREAD_GRAYSCALE)
#im=cv2.imread("images\\rubiks1.jpg", cv2.IMREAD_GRAYSCALE)

#im = cv2.GaussianBlur(im, (5, 5), 0)
#im = cv2.bilateralFilter(im,15,75,75)
#im = cv2.bilateralFilter(im, 11, 17, 17)
edged = cv2.Canny(im_bw, 20, 40)


cv2.imshow("edged", edged)

#now let's dialate the lines
kernel = np.ones((10,10), np.uint8)
dilated = cv2.dilate(edged, kernel, iterations=1)

cv2.imshow("dilated", dilated)

#im2, cnts, hierarchy = cv2.findContours(im, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
im2, cnts, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(im, contours, -1, (0,255,0), 3)
#cv2.imshow("final", im)

sq_cont=[]
contour_centers=[]
for contour in cnts:
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.1 * peri, True)
    x, y, w, h = cv2.boundingRect(approx)
    sq_cont.append(contour)
    m = cv2.moments(contour)
    cx = int(m["m10"] / m["m00"])
    cy = int(m["m01"] / m["m00"])
    contour_centers.append([cx,cy])
            
cv2.drawContours(im, sq_cont, -1, (0,255,0), 3)
cv2.imshow("final", im)

contour_centers.sort(key=sortSecond)











