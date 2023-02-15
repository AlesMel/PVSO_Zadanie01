from time import sleep
import cv2 as cv
import numpy as np
def setup_camera():
    cam = cv.VideoCapture(0)
    return cam

def process_image(width, height):
    ret, img = cam.read()
    image = cv.resize(img, (width, height))
    return image


def append_image(msc, cur_img):
    np.append(msc, cur_img)
    return msc

cam = setup_camera()
cur_index = 0
mosaic = np.empty((400, 300, 4, 4))
print(mosaic)

while True:
    processed_image = process_image(400, 300)
    pressed = cv.waitKey(1)
    if pressed == ord(' '):
        mosaic = append_image(mosaic, processed_image)
        cv.imwrite("pekne_fotky_{0}.jpg".format(cur_index), processed_image)
        cur_index += 1
    elif pressed == ord('q'):
        break
    cv.imshow("Image", processed_image)

print("ARRAY -- ")
print(np.array(mosaic))
cv.imwrite("mosaic.jpg", mosaic)

cam.stop_acquisition()
cam.close_device()
