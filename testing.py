import numpy as np
import cv2 as cv
import image_processing as ip


# [0-400, 0-300] 2. [400-800, 0-300], 3. [0-400, 300-600], 4. [400-800, 300-600]

def divide_images(images, ratio):
    mozaic_height, mozaic_width, depth = images.shape

    # # individiual img size
    img_height = mozaic_height // ratio[1]
    img_width = mozaic_width // ratio[0]

    # divide images along height
    divided_images = np.split(images, ratio[0], axis=0)

    # divide images along width
    for i in range(len(divided_images)):
        divided_images[i] = np.split(divided_images[i], ratio[1], axis=1)

    return divided_images
    # Show the individual image
    # for i in range(len(divided_images)):
    #     for j in range(len(divided_images[i])):
    #         cv.imshow(f"Divided Image ({i},{j})", divided_images[i][j])

def show_images(images):
    for i in range(len(images)):
        for j in range(len(images[i])):
            cv.imshow(f"Divided Image ({i},{j})", images[i][j])

def apply_kernel(images, image_number, kernel):
    # Calculate the row and column indices for the selected sub-image
    row_index = (image_number - 1) // 2
    col_index = (image_number - 1) % 2

    # Slice the 3D numpy array to extract the corresponding 2D numpy array
    img = images[row_index * 300:(row_index + 1) * 300, col_index * 400:(col_index + 1) * 400]
    filtered_image = cv.filter2D(img, -1, kernel)

    # Replace the original image with the filtered image in the 3D numpy array
    images[row_index*300:(row_index+1)*300, col_index*400:(col_index+1)*400] = filtered_image
    return images


kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

lower = np.array([155,25,0])
upper = np.array([179,255,255])
red_kernel = np.ones((15,15),np.float32)/225
imgs = ip.apply_kernel(cv.imread("Images/mosaic.jpg"), 1, kernel, width=400, height=400)
imgs = ip.apply_color(imgs, 3, "red", 400, 400)
imgs = ip.rotate_images(imgs, 90, image_number=3, height=400, width=400)
cv.imwrite('Image/modified_mosaic.jpg', imgs)
cv.imshow('modified_mosaic.jpg', imgs)

# divided_images = apply_kernel(kernel, divided_images, 2)

color_switcher = {
    "blue": 0,
    "green": 1,
    "red": 2,
}

cv.waitKey(0)
cv.destroyAllWindows()
