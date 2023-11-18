import os

from PIL import Image
from svglib.svglib import svg2rlg

# 图片格式支持：  png jpg bmp
# TODO :  webp svg
path_in = r'data'
path_out = r'result'

# 单次与多次
def imgConvert(path_in,target_format):
    """
    param path_in: 原图片路径
    :param target_format:  图片输出格式
    :return bool：是否成功
    """
    Dir_img = path_in.split('.')[0]
    format_list = ['.jpg', '.png', '.jpeg', '.webp', '.bmp', '.tiff']
    with Image.open(path_in) as source_img:
        src_format = source_img.format
        src_mode = source_img.mode
        if src_format != target_format:
            source_img = source_img.convert('RGB')  # 将源图像convert到PIL支持的mode
            target_img = Image.new(src_mode, source_img.size)  # 创建目标对象
            target_img.putdata(list(source_img.getdata()))  # 将像素从源图像复制到目标图像
            file_name = f'{Dir_img}.{target_format}'
            target_img.save(file_name)
            print('Convert to {} successfully'.format(target_format))
        else:
            print('formats are the same,no need to convert 😅')





if __name__ == '__main__' :
    imgConvert('data/img.png','jpg')


