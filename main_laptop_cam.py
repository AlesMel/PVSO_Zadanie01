from time import sleep
import cv2 as cv
import numpy as np

WIDTH: int = 400
HEIGHT: int = 400


def setup_camera():
    cam = cv.VideoCapture(0)
    return cam


def post_process_image(image: np.ndarray, kernel: np.ndarray,
                       img_index_x: int = 1, img_index_y: int = 1):
    if isinstance(image, np.ndarray):
        height = image.shape[0]
        width = image.shape[1]

        # Kernel
        processed_part = cv.filter2D(np.array(image[:int(height / 2), :int(width / 2)]), -1, kernel)
        image[:int(height / 2), :int(width / 2)] = processed_part

        # Color channel
        image[int(height / 2):, int(width / 2):, 0] = 0  # Blue
        image[int(height / 2):, int(width / 2):, 1] = 0  # Green
        # image[int(height / 2):, int(width / 2):, 2] = 0  # Red

        cv.imshow("image", image)
        cv.waitKey()
        return True
    return False


def process_image(width, height):
    ret, img = cam.read()
    image = cv.resize(img, (width, height))
    return image


def concat_images(images):
    return cv.vconcat([cv.hconcat(img) for img in images])


cam = setup_camera()
cur_index = 0
image_data = []

while cur_index < 4:
    processed_image = process_image(WIDTH, HEIGHT)
    pressed = cv.waitKey(1)
    if pressed == ord(' '):
        image_data.append(processed_image)
        # Apply kernel
        cv.imwrite("pekne_fotky_{0}.jpg".format(cur_index), processed_image)
        cur_index += 1
    elif pressed == ord('q'):
        break
    cv.imshow("Image", processed_image)

# now concat the data but reshape them first to be 2x2 grid
result = concat_images(np.array(image_data).reshape(2, 2, HEIGHT, WIDTH, 3))

# save the image as mosaic.jpg
cv.imwrite("mosaic.jpg", np.array(result))

# Post process mosaic
mosaic = cv.imread("mosaic.jpg")

kernel = np.array([[-1, -1, -1],
                   [-1, 8, -1],
                   [-1, -1, -1]])
post_process_image(mosaic, kernel)

# cv.imshow("image", mosaic)
# cv.waitKey()

# After the loop release the cap object
cam.release()
# Destroy all the windows
cv.destroyAllWindows()
