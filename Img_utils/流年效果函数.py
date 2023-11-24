import cv2
import math
import numpy as np

class ImgProcess:
    def __init__(self, img) -> None:
        self.src = cv2.imread(img)
        self.h, self.w = self.src.shape[:2]

    def fleet(self, output_path):
        fleetImg = np.zeros((self.h, self.w, 3), np.uint8)
        for i in range(self.h):
            for j in range(0, self.w):
                b = math.sqrt(self.src[i, j][0]) * 14
                g = self.src[i, j][1]
                r = self.src[i, j][2]
                if b > 255:
                    b = 255
                fleetImg[i, j] = np.uint8((b, g, r))

        # Save the processed image
        cv2.imwrite(output_path, fleetImg)
        return fleetImg

# 创建 ImgProcess 类的实例，指定图像文件路径
process = ImgProcess('C:\\Users\\zjr\\Desktop\\7ca185dd956ef6e0ee03e7c48559540.jpg')

# 指定输出路径
output_path = 'C:\\Users\\zjr\\Desktop\\processed_image.jpg'

# 调用流年效果并保存到指定路径
fleetImg = process.fleet(output_path)

# 显示流年效果
cv2.imshow("Fleet", cv2.resize(fleetImg, (400, 400)))
cv2.waitKey(0)
cv2.destroyAllWindows()
