from PIL import Image, ImageEnhance
 
# 打开原图像
img = Image.open("D:\\工作目录\cc\\task01\input.png")
 
# 设置增强因子
enhancer = ImageEnhance.Sharpness(img)
factor = 2.0
 
# 增强图片
img_enhanced = enhancer.enhance(factor)
 
# 保存增强后的图像
img_enhanced.save("D:\\工作目录\cc\\task01\output.png")