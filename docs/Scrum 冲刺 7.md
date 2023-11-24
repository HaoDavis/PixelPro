| 这个作业属于哪个课程 | [软件工程](https://edu.cnblogs.com/campus/gdgy/CSGrade21-12) |
| :-----------------: |:---------------: |
| 这个作业要求在哪里 | [团队作业4——项目冲刺](https://edu.cnblogs.com/campus/gdgy/CSGrade21-12/homework/13020) |
| 这个作业的目标 | 记录昨日已完成工作，明确今日工作，总结项目进度 |

# 敏捷冲刺日志集合
[项目冲刺集合贴](https://www.cnblogs.com/notingblogs/p/17840948.html)

# 站立会议
## 会议照片
因每个人不单有软工项目，在线下时间上凑齐所有人较为困难，所以我们采用微信会议的方式进行。
![image](https://img2023.cnblogs.com/blog/3270285/202311/3270285-20231119081324179-2117685492.png)

## 会议内容
| 成员 | 昨日完成 | 今日计划 | 遇到的困难 |
|:----:|:---:|:------------:|:---------:|
| 戴子豪 | 编写博客 Scrum 冲刺 6 及 Scrum 冲刺集合贴、组织站立会议、绘制项目燃尽图。  | 编写博客 Scrum 冲刺 7 及 更新 Scrum 冲刺集合贴、组织站立会议、绘制项目燃尽图。 | 成员在时间上很难凑齐，讨论积极性欠缺。 |
| 朱俊荣 | 编写了图片风格化的多个函数，另外优化了post请求。 | 优化算法缩短风格化函数的执行时间。 | cv等库中封装的函数参数众多，处理图像同时较长。 |
| 李铭伟 | 之前部分功能的完善。| 尽可能添加新功能以及测试。  | 缺乏交流。 |
| 陈倚星 | 完成了用鼠标进行图片裁剪的代码 | 进一步完善细节。 | 基本可以在网上找到解决方法。|
| 卫宇琪 | OCR功能的收尾。 | 图片清晰化和图片涂鸦。 | 测试过程存在问题。 |
| 张震 | 完成了三个模块的单元测试。 | 总结问题。 | 库的安装遇到很多报错。 |
| 甫尔达吾斯 | 代码测试。 | 测试。 | 不断出现漏洞，代码还需要测试。 |

# 项目燃尽图
![image](https://img2023.cnblogs.com/blog/3270285/202311/3270285-20231124104630700-37434383.png)

# 签入记录
## 代码/文档签入记录
![image](https://img2023.cnblogs.com/blog/3270285/202311/3270285-20231124104728549-949901868.png)

![image](https://img2023.cnblogs.com/blog/3270285/202311/3270285-20231124104749780-226840421.png)

## 对应的 Issue 内容与链接
| 成员 | Issue 内容与链接 |
|:----:|:---:|
| 戴子豪 | [团队博客](https://github.com/HaoDavis/PixelPro/issues/13) |
| 朱俊荣 | [整体结合](https://github.com/HaoDavis/PixelPro/issues/14) |
| 李铭伟 | [各功能完善](https://github.com/HaoDavis/PixelPro/issues/8) |
| 陈倚星 | [自由大小裁剪](https://github.com/HaoDavis/PixelPro/issues/4) |
| 卫宇琪 | [图片文字识别](https://github.com/HaoDavis/PixelPro/issues/11) |
| 张震 | [功能测试](https://github.com/HaoDavis/PixelPro/issues/14) |
| 甫尔达吾斯 | [证件照换底色](https://github.com/HaoDavis/PixelPro/issues/6) |
## Code Review 编码规范文档状态
无变化
# 项目进度
## 部分模块代码
图片风格化-怀旧风：
```python
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
```
图片风格化-油画
```python
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
```
图片风格化-流年效果
```python
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
```
图片风格化-素描风
```python
from PIL import Image    #图像处理模块
import numpy as np

a = np.asarray(Image.open("C:\\Users\\zjr\\Desktop\\7ca185dd956ef6e0ee03e7c48559540.jpg").convert('L')).astype('float')    #将图像以灰度图的方式打开并将数据转为float存入np中

depth = 10.                      # (0-100)
grad = np.gradient(a)             #取图像灰度的梯度值
grad_x, grad_y =grad               #分别取横纵图像梯度值
grad_x = grad_x*depth/100.
grad_y = grad_y*depth/100.
A = np.sqrt(grad_x**2 + grad_y**2 + 1.)
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A
#建立一个位于图像斜上方的虚拟光源
vec_el = np.pi/2.2                   # 光源的俯视角度，弧度值
vec_az = np.pi/4.                    # 光源的方位角度，弧度值
dx = np.cos(vec_el)*np.cos(vec_az)   #光源对x 轴的影响
dy = np.cos(vec_el)*np.sin(vec_az)   #光源对y 轴的影响
dz = np.sin(vec_el)                  #光源对z 轴的影响
#计算各点新的像素值
b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)     #光源归一化
b = b.clip(0,255)    #clip函数将区间外的数字剪除到区间边缘

im = Image.fromarray(b.astype('uint8'))  #重构图像
im.save("C:\\Users\\zjr\\Desktop\\7ca185dd956ef6e0ee03e7c48559540.jpg")
```
## 部分运行结果
![image](https://img2023.cnblogs.com/blog/3270285/202311/3270285-20231122130341614-1338921857.png)

# 总结
| 成员 | 总结 |
|:----:|:---:|
| 戴子豪 | 团队协作耗时较长、实际编写代码只是一小部分。 |
| 朱俊荣 | cv函数需要不断调参来达到理想效果。 |
| 李铭伟 | 仍需要极大程度沉淀。 |
| 陈倚星 | 还是要由易到难。 |
| 卫宇琪 | 边学习边成长。 |
| 张震 | 一步步解决，直到完成。 |
| 甫尔达吾斯 | 还需要继续完善。 |