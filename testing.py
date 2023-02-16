import numpy as np
import cv2 as cv


# mosaic = np.empty((4, 3, 4, 4,))
# mosaic2 = mosaic.reshape(2, 2, 3, 4, 4)
# print(mosaic)
# print(mosaic.shape)
# print(mosaic2)

# Test dimensions
# def post_process_image(image: np.ndarray, kernel: np.ndarray,
#                        img_index_x: int = 1, img_index_y: int = 1):
#     if isinstance(image, np.ndarray):
#         height = image.shape[0]
#         width = image.shape[1]
#
#         # Calculate corresponding dimensions
#         processed_part = cv.filter2D(np.array(image[:int(height / 2), :int(width / 2)]), -1, kernel)
#         image[:int(height / 2), :int(width / 2)] = processed_part
#
#         cv.imshow("image", image)
#         cv.waitKey()
#
#         return True
#     return False


post_process_image(cv.imread("mosaic.jpg"), np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]))
