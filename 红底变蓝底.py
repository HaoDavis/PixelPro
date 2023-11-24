import cv2
import numpy as np

# 读取照片
img = cv2.imread('C:\\Users\\Administrator\\Desktop\\yang.jpg')

# 图像缩放
img = cv2.resize(img, None, fx=0.5, fy=0.5)
rows, cols, channels = img.shape
print(rows, cols, channels)
cv2.imshow('img', img)

# 图片转换为HSV色彩空间
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', hsv)

# 图片的二值化处理
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
mask = cv2.inRange(hsv, lower_red, upper_red)

# 腐蚀膨胀
erode = cv2.erode(mask, None, iterations=1)
cv2.imshow('erode', erode)

dilate = cv2.dilate(erode, None, iterations=1)
cv2.imshow('dilate', dilate)
import cv2
import numpy as np

# 读取照片并显示
image=cv2.imread('C:\\Users\\Administrator\\Desktop\\yang.jpg')
cv2.imshow('image',image)

# 图像缩放并显示
img = cv2.resize(image,None,fx=0.5,fy=0.5)
rows,cols,channels = img.shape
print(rows,cols,channels)
cv2.imshow('img',img)

# 图片转换为灰度图
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv',hsv)

# 图片的二值化处理
# 将在两个阈值内的像素值设置为白色（255），而不在阈值区间内的像素值设置为黑色（0），该功能类似于之间所讲的双阈值化操作
# 红底变白底
lower_blue = np.array([0,135,135])
upper_blue = np.array([180,245,230])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
# 显示图像
cv2.imshow('mask',mask)




#腐蚀膨胀
erode=cv2.erode(mask,None,iterations=1)
cv2.imshow('erode',erode)

dilate=cv2.dilate(erode,None,iterations=1)
cv2.imshow('dilate',dilate)

# 遍历每个像素点，进行颜色的替换
for i in range(rows):
  for j in range(cols):
    if dilate[i,j]==255:    # 像素点为255表示的是白色，我们就要将白色处的像素点，替换为你想要的照片底色
      img[i,j]=(255,0,0)    # 此处替换颜色，为BGR通道，不是RGB通道，若是想要将红底变成蓝底img[i,j]=(255,0,0)，若是想讲蓝底变为红底则img[i,j]=(0,0,255)
      # img[i, j] = (0, 0, 255)
      # img[i, j] = (255, 255, 255)  # 变白底
cv2.imshow('res',img)


# 窗口等待的命令，0表示无限等待
cv2.waitKey(0)
# 遍历每个像素点，进行颜色的替换
for i in range(rows):
    for j in range(cols):
        if erode[i, j] == 255:  # 像素点为255表示的是白色，我们就是要将白色处的像素点，替换为蓝色
            img[i, j] = (255, 0, 0)  # 此处替换颜色，为BGR通道，不是RGB通道
cv2.imshow('res', img)

# 窗口等待的命令，0表示无限等待
cv2.waitKey(0)
