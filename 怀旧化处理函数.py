import cv2
import numpy as np

class ImgProcess:
    def __init__(self, img) -> None:
        self.src = cv2.imread(img)
        self.h, self.w = self.src.shape[:2]

    def old(self):
        oldImg = np.zeros_like(self.src)

        b = 0.272 * self.src[:, :, 2] + 0.534 * self.src[:, :, 1] + 0.131 * self.src[:, :, 0]
        g = 0.349 * self.src[:, :, 2] + 0.686 * self.src[:, :, 1] + 0.168 * self.src[:, :, 0]
        r = 0.393 * self.src[:, :, 2] + 0.769 * self.src[:, :, 1] + 0.189 * self.src[:, :, 0]

        oldImg[:, :, 0] = np.clip(b, 0, 255).astype(np.uint8)
        oldImg[:, :, 1] = np.clip(g, 0, 255).astype(np.uint8)
        oldImg[:, :, 2] = np.clip(r, 0, 255).astype(np.uint8)

        return oldImg

# 创建ImgProcess类的实例，指定图像文件路径
process = ImgProcess('C:\\Users\\zjr\\Desktop\\7ca185dd956ef6e0ee03e7c48559540.jpg')

# 调用怀旧效果
oldImg = process.old()

# 显示怀旧效果
cv2.imshow("Old Photo", cv2.resize(oldImg, (400, 400)))
cv2.waitKey(0)
cv2.destroyAllWindows()
