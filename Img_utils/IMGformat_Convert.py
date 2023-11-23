import os

import threading
from PIL import Image
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from glob import glob

# 图片格式支持：  png jpg bmp
path_in = r'data'
path_out = r'result'
FORMAT = ['PNG', 'JPG', 'BMP', 'SVG', 'JFIF', 'WEBP']


# 单次与多次
def img2Convert(path_in, target_format):
    """
    param path_in: 原图片路径
    :param target_format:  图片输出格式
    """
    Dir_img, src_format= path_in.split('.')[0],path_in.split('.')[1]
    if src_format == 'svg':
        drawing = svg2rlg(path_in)
        renderPM.drawToFile(drawing,Dir_img+'.'+target_format,fmt=target_format.upper())
    with Image.open(path_in) as source_img:
        src_mode = source_img.mode
        has_alpha = 'A' in src_mode # bool
        if src_format != target_format:
            source_img = source_img.convert('RGB')  # 将源图像convert到PIL支持的mode
            target_img = Image.new(src_mode, source_img.size)  # 创建目标对象
            target_img.putdata(list(source_img.getdata()))  # 将像素从源图像复制到目标图像
            file_name = f'{Dir_img}.{target_format}'
            target_img.save(file_name)
            print('Convert to {} successfully'.format(target_format))
        else:
            print('formats are the same,no need to convert 😅')

def img_folder2Convert(file_folder,target_format):
    threads=[]
    for img in glob(file_folder + '\\*'):
        img_format = img.split('.')[1].upper()
        if img_format not in FORMAT:
            raise ValueError('The format of {} is not support'.format(img))
        t=threading.Thread(target=img2Convert,args=(f,target_format))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


