import numpy as np
import cv2 as cv
import image_processing as ip
rows = 2
cols = 2
img = ip.rotate_image(cv.imread("Images/mosaic.jpg"), 3, 400, 400)
cv.imshow("wtf", img)
cv.waitKey()