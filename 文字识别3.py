import pytesseract
from PIL import Image

# 加载图片
img = Image.open('C:\\Users\\Administrator\\Desktop\\sb.png')

# 转换为灰度图像
img = img.convert('L')

# 识别文本, 使用pytesseract库进行OCR识别, 将语言设置成中文
text = pytesseract.image_to_string(img, lang='chi_sim')
# 输出识别结果
print(text)
