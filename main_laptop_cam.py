from time import sleep
import cv2 as cv
import numpy as np

WIDTH = 400
HEIGHT = 300


def setup_camera():
    cam = cv.VideoCapture(0)
    return cam


def process_image(width, height):
    ret, img = cam.read()
    image = cv.resize(img, (width, height))
    return image


def concat_images(images):
    return cv.vconcat([cv.hconcat(img) for img in images])


cam = setup_camera()
cur_index = 0
image_data = []

# Edge detection kernel
kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

while cur_index < 4:
    processed_image = process_image(400, 300)
    pressed = cv.waitKey(1)
    if pressed == ord(' '):

        if cur_index == 0:
            # If it's first image apply kernel
            processed_image = cv.filter2D(processed_image, -1, kernel)

        image_data.append(processed_image)
        # Apply kernel
        cv.imwrite("pekne_fotky_{0}.jpg".format(cur_index), processed_image)
        cur_index += 1
    elif pressed == ord('q'):
        break
    cv.imshow("Image", processed_image)

# check the shape
print(np.array(image_data).shape)

# now concat the data but reshape them first to be 2x2 grid
result = concat_images(np.array(image_data).reshape(2, 2, 300, 400, 3))

# save the image as mosaic.jpg
cv.imwrite("mosaic.jpg", np.array(result))

# After the loop release the cap object
cam.release()
# Destroy all the windows
cv.destroyAllWindows()
