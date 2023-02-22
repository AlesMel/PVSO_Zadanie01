import cv2 as cv
import numpy as np


def process_image(cam, width, height):
    ret, img = cam.read()
    image = cv.resize(img, (width, height))
    return image


def concat_images(images):
    return cv.vconcat([cv.hconcat(img) for img in images])


def apply_kernel(images, image_number, kernel, width, height):
    assert image_number != 0
    # Calculate the row and column indices for the selected sub-image
    row_index = (image_number - 1) // 2
    col_index = (image_number - 1) % 2

    # Slice the 3D numpy array to extract the corresponding 2D numpy array
    img = images[row_index * height:(row_index + 1) * height, col_index * width:(col_index + 1) * width]
    filtered_image = cv.filter2D(img, -1, kernel)

    # Replace the original image with the filtered image in the 3D numpy array
    images[row_index * height:(row_index + 1) * height, col_index * width:(col_index + 1) * width] = filtered_image
    return images


def apply_color(images, image_number, color, width, height):
    color_switcher = {
        "blue": 0,
        "green": 1,
        "red": 2,
    }

    assert image_number != 0
    # Calculate the row and column indices for the selected sub-image
    row_index = (image_number - 1) // 2
    col_index = (image_number - 1) % 2

    # Slice the 3D numpy array to extract the corresponding 2D numpy array
    img = images[row_index * height:(row_index + 1) * height, col_index * width:(col_index + 1) * width]
    chosen_color = color_switcher.get(color, -1)

    # hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    #
    # lower_red = np.array([0, 50, 50])
    # upper_red = np.array([10, 255, 255])

    # mask = cv.inRange(hsv_img, lower_red, upper_red)
    # img = cv.bitwise_and(img, img, mask=mask)

    for i in range(3):
        if i != chosen_color:
            img[:, :, i] = 0

    # Replace the original image with the filtered image in the 3D numpy array
    images[row_index * height:(row_index + 1) * height, col_index * width:(col_index + 1) * width] = img
    return images


def divide_images(images, ratio):
    mozaic_height, mozaic_width, depth = images.shape

    # individiual img size
    img_height = mozaic_height // ratio[1]
    img_width = mozaic_width // ratio[0]

    # divide images along height
    divided_images = np.split(images, ratio[0], axis=0)

    # divide images along width
    for i in range(len(divided_images)):
        divided_images[i] = np.split(divided_images[i], ratio[1], axis=1)

    return divided_images


def rotate_images(images, angle, image_number, height, width):
    row_index = (image_number - 1) // 2
    col_index = (image_number - 1) % 2
    extracted_image = images[row_index * height:(row_index + 1) * height, col_index * width:(col_index + 1) * width]
    img_size = (height, width)
    center = (img_size[0] // 2, img_size[1] // 2)
    rot_matrix = cv.getRotationMatrix2D(center, angle, 1.0)
    rotated_tile = cv.warpAffine(extracted_image, rot_matrix, img_size)
    images[row_index * height:(row_index + 1) * height, col_index * width:(col_index + 1) * width] = rotated_tile
    return images
