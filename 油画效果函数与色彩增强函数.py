import cv2
import numpy as np
from PIL import Image, ImageEnhance
import random


# 油画效果
def oil_effect(img):
    h, w, n = img.shape
    new_img = np.zeros((h - 2, w, n), dtype=np.uint8)
    for i in range(h - 2):
        for j in range(w):
            if random.randint(1, 10) % 3 == 0:
                new_img[i, j] = img[i - 1, j]
            elif random.randint(1, 10) % 2 == 0:
                new_img[i, j] = img[i + 1, j]
            else:
                new_img[i, j] = img[i + 2, j]
    return new_img


# 图像增强
def img_add(img_path):
    img = Image.open(img_path)
    enh_col = ImageEnhance.Color(img)
    color = 2.0
    new_img = enh_col.enhance(color)
    new_img = cv2.cvtColor(np.asarray(new_img), cv2.COLOR_RGB2BGR)
    return new_img


if __name__ == "__main__":
    input_image_path = "C:\\Users\\zjr\\Desktop\\7ca185dd956ef6e0ee03e7c48559540.jpg"
    img = cv2.imread(input_image_path)

    oil_img = oil_effect(img)
    cv2.imwrite("oil.jpg", oil_img)

    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Image with Color Enhancement", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Oil Painting Effect", cv2.WINDOW_NORMAL)

    cv2.resizeWindow("Original Image", 800, 800)
    cv2.resizeWindow("Image with Color Enhancement", 800, 800)
    cv2.resizeWindow("Oil Painting Effect", 800, 800)

    cv2.imshow("Original Image", img)
    cv2.imshow("Image with Color Enhancement", img_add(input_image_path))
    cv2.imshow("Oil Painting Effect", oil_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
