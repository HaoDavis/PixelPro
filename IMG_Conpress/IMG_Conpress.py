import os
import logging

from PIL import Image


MIN_QUALITY = 20

def get_size(filename):
    return os.path.getsize(filename)

def conpress_image(file_in, file_out='',mb=1500):
    """
    compress image without changing any img_size
    :param file_in: 源文件
    :param file_out:  out地址
    :param mb: 大小
    :param step:  调整比率
    :param equlity: 初始压缩比率
    :return:  压缩文件地址
    """
    if not os.path.exists(file_in):
        raise FileNotFoundError

    Dir, fmt = file_in.split('.')
    file_out = Dir + '_out.' + fmt if file_out == '' else file_out

    quality = 80
    while True:
        img = Image.open(file_in)
        img.save(file_out,quality=quality)

        size = get_size(file_out)
        a_size = size/1024
        if a_size<=mb or quality < MIN_QUALITY:
            break

        quality -=10

    return file_out,size

if __name__ == '__main__':
    conpress_image('computer_kuan_201632_18.jpg')