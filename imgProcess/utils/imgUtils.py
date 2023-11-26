import math
import random

import cv2
import numpy as np
from PIL import Image, ImageEnhance
import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

MIN_QUALITY = 20


def get_size(filename):
    return os.path.getsize(filename)


def compress_image(file_in, file_out=None, target_size=1024):
    """
    compress image without changing any img_size
    :param file_in: 源文件
    :param file_out:  out地址
    :param target_size: 大小 单位KB
    :return:  压缩文件地址
    """
    if not os.path.exists(file_in):
        raise FileNotFoundError

    basename, ext = os.path.splitext(os.path.basename(file_in))
    file_out = file_out or f'{basename}_compressed{ext}'

    try:
        quality = 50
        while True:
            with Image.open(file_in) as img:
                img.save(file_out, quality=quality)

            size = get_size(file_out)

            if size / 1024 <= target_size or quality < MIN_QUALITY:
                break

            quality -= 10
    except Exception as e:
        pass

    return file_out, get_size(file_out)


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


def getOldImg(file_in, file_out):
    process = ImgProcess(file_in)
    oldImg = process.old()
    image = cv2.cvtColor(oldImg, cv2.COLOR_BGR2RGB)
    cv2.imwrite(file_out, image)
    return True


# 油画效果
def oil_effect(file_in, file_out):
    img = cv2.imread(file_in)
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
    cv2.imwrite(file_out, new_img)
    return True


# 图像增强
def img_add(file_in, file_out):
    img = Image.open(file_in)
    enh_col = ImageEnhance.Color(img)
    color = 2.0
    new_img = enh_col.enhance(color)
    new_img = cv2.cvtColor(np.asarray(new_img), cv2.COLOR_RGB2BGR)
    cv2.imwrite(file_out, new_img)
    return new_img


def sketch(file_in, file_out):
    a = np.asarray(Image.open(file_in).convert('L')).astype('float')  # 将图像以灰度图的方式打开并将数据转为float存入np中

    depth = 10.  # (0-100)
    grad = np.gradient(a)  # 取图像灰度的梯度值
    grad_x, grad_y = grad  # 分别取横纵图像梯度值
    grad_x = grad_x * depth / 100.
    grad_y = grad_y * depth / 100.
    A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
    uni_x = grad_x / A
    uni_y = grad_y / A
    uni_z = 1. / A
    # 建立一个位于图像斜上方的虚拟光源
    vec_el = np.pi / 2.2  # 光源的俯视角度，弧度值
    vec_az = np.pi / 4.  # 光源的方位角度，弧度值
    dx = np.cos(vec_el) * np.cos(vec_az)  # 光源对x 轴的影响
    dy = np.cos(vec_el) * np.sin(vec_az)  # 光源对y 轴的影响
    dz = np.sin(vec_el)  # 光源对z 轴的影响
    # 计算各点新的像素值
    b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  # 光源归一化
    b = b.clip(0, 255)  # clip函数将区间外的数字剪除到区间边缘

    im = Image.fromarray(b.astype('uint8'))  # 重构图像
    im.save(file_out)


def fleet(file_in, file_out):
    src = cv2.imread(file_in)
    h, w = src.shape[:2]
    fleetImg = np.zeros((h, w, 3), np.uint8)
    for i in range(h):
        for j in range(0, w):
            b = math.sqrt(src[i, j][0]) * 14
            g = src[i, j][1]
            r = src[i, j][2]
            if b > 255:
                b = 255
            fleetImg[i, j] = np.uint8((b, g, r))

    # Save the processed image
    cv2.imwrite(file_out, fleetImg)
    return True


def resizeImg(file_in, file_out, h, w):
    # 打开图像文件
    original_image = Image.open(file_in)

    # 指定目标大小
    target_size = (h, w)

    # 使用resize方法调整图像大小
    resized_image = original_image.resize(target_size)

    # 保存调整大小后的图像
    resized_image.save(file_out)


def convertImg(file_in, file_out, target_format):
    """
    param path_in: 原图片路径
    :param target_format:  图片输出格式
    :return bool：是否成功
    """
    Dir_img, src_format = file_in.split('.')[0], file_in.split('.')[1]
    if src_format == 'svg':
        drawing = svg2rlg(file_in)
        renderPM.drawToFile(drawing, Dir_img + '.' + target_format, fmt=target_format.upper())
    with Image.open(file_in) as source_img:
        src_mode = source_img.mode
        source_img = source_img.convert('RGB')  # 将源图像convert到PIL支持的mode
        target_img = Image.new(src_mode, source_img.size)  # 创建目标对象
        target_img.putdata(list(source_img.getdata()))  # 将像素从源图像复制到目标图像
        file_name = f'{Dir_img}.{target_format}'
        target_img.save(file_out)
        print('Convert to {} successfully'.format(target_format))


import pytesseract


def readText(file_in):
    # 加载图片
    img = Image.open(file_in)

    # 转换为灰度图像
    img = img.convert('L')

    # 识别文本, 使用pytesseract库进行OCR识别, 将语言设置成中文
    text = pytesseract.image_to_string(img, lang='chi_sim')
    return text


def redBg(file_in, file_out):
    img = cv2.imread(file_in)
    # 图像缩放
    img = cv2.resize(img, None, fx=0.5, fy=0.5)
    rows, cols, channels = img.shape

    # 图片转换为灰度图
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv', hsv)

    # 图片的二值化处理
    lower_blue = np.array([90, 70, 70])
    upper_blue = np.array([110, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # 腐蚀膨胀
    erode = cv2.erode(mask, None, iterations=1)

    dilate = cv2.dilate(erode, None, iterations=1)

    # 遍历每个像素点，进行颜色的替换
    for i in range(rows):
        for j in range(cols):
            if erode[i, j] == 255:  # 像素点为255表示的是白色，我们就是要将白色处的像素点，替换为红色
                img[i, j] = (0, 0, 255)  # 此处替换颜色，为BGR通道，不是RGB通道
    cv2.imwrite(file_out, img)


def blueBg(file_in, file_out):
    # 读取照片并显示
    image = cv2.imread(file_in)
    # 图像缩放并显示
    img = cv2.resize(image, None, fx=0.5, fy=0.5)
    rows, cols, channels = img.shape
    # 图片转换为灰度图
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([0, 135, 135])
    upper_blue = np.array([180, 245, 230])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)


    # 腐蚀膨胀
    erode = cv2.erode(mask, None, iterations=1)

    dilate = cv2.dilate(erode, None, iterations=1)

    # 遍历每个像素点，进行颜色的替换
    for i in range(rows):
        for j in range(cols):
            if dilate[i, j] == 255:  # 像素点为255表示的是白色，我们就要将白色处的像素点，替换为你想要的照片底色
                img[i, j] = (
                255, 0, 0)  # 此处替换颜色，为BGR通道，不是RGB通道，若是想要将红底变成蓝底img[i,j]=(255,0,0)，若是想讲蓝底变为红底则img[i,j]=(0,0,255)
                # img[i, j] = (0, 0, 255)
                # img[i, j] = (255, 255, 255)  # 变白底

    # 窗口等待的命令，0表示无限等待
    cv2.waitKey(0)
    # 遍历每个像素点，进行颜色的替换
    for i in range(rows):
        for j in range(cols):
            if erode[i, j] == 255:  # 像素点为255表示的是白色，我们就是要将白色处的像素点，替换为蓝色
                img[i, j] = (255, 0, 0)  # 此处替换颜色，为BGR通道，不是RGB通道
    cv2.imwrite(file_out, img)


def whiteBg(file_in, file_out):
    # 读取照片并显示
    image = cv2.imread(file_in)
    # 图像缩放并显示
    img = cv2.resize(image, None, fx=0.5, fy=0.5)
    rows, cols, channels = img.shape
    # 图片转换为灰度图
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv', hsv)

    lower_blue = np.array([0, 135, 135])
    upper_blue = np.array([180, 245, 230])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # 腐蚀膨胀
    erode = cv2.erode(mask, None, iterations=1)

    dilate = cv2.dilate(erode, None, iterations=1)

    # 遍历每个像素点，进行颜色的替换
    for i in range(rows):
        for j in range(cols):
            if dilate[i, j] == 255:  # 像素点为255表示的是白色，我们就要将白色处的像素点，替换为你想要的照片底色
                # img[i,j]=(255,0,0)    # 此处替换颜色，为BGR通道，不是RGB通道，若是想要将红底变成蓝底img[i,j]=(255,0,0)，若是想讲蓝底变为红底则img[i,j]=(0,0,255)
                # img[i, j] = (0, 0, 255)
                img[i, j] = (255, 255, 255)  # 变白底
    # 遍历每个像素点，进行颜色的替换
    for i in range(rows):
        for j in range(cols):
            if erode[i, j] == 255:  # 像素点为255表示的是白色，我们就是要将白色处的像素点，替换为蓝色
                img[i, j] = (255, 0, 0)  # 此处替换颜色，为BGR通道，不是RGB通道
    cv2.imwrite(file_out, img)


def convertColor(file_in, file_out,  color):
    if color == 'red':
        redBg(file_in, file_out)
    elif color == 'blue':
        blueBg(file_in, file_out)
    elif color == 'white':
        whiteBg(file_in, file_out)


keyToFunc = {
    'compress_image': compress_image,
    'getOldImg': getOldImg,
    'oil_effect': oil_effect,
    'img_add': img_add,
    'fleet': fleet,
    'sketch': sketch,
    'resizeImg': resizeImg,
    'convertImg': convertImg,
    'readText': readText,
    'convertColor': convertColor,
}

if __name__ == '__main__':
    fleet('./task2.png', './test.png')
