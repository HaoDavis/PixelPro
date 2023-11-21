import os
import logging
import tempfile

from PIL import Image

logging.basicConfig(filename='compress.log',level=logging.DEBUG)

MIN_QUALITY = 20

def get_size(filename):
    return os.path.getsize(filename)

def conpress_image(file_in, file_out=None,target_size=1500):
    """
    compress image without changing any img_size
    :param file_in: 源文件
    :param file_out:  out地址
    :param target_size: 大小 单位KB
    :return:  压缩文件地址
    """
    if not os.path.exists(file_in):
        raise FileNotFoundError


    basename,ext = os.path.splitext(os.path.basename(file_in))
    file_out = file_out or f'{basename}_compressed{ext}'

    logging.info(f'Compressing {file_in} to {file_out}')

    try:
        quality = 50
        while True:
            with Image.open(file_in) as img:
                img.save(file_out,quality=quality)

            size = get_size(file_out)
            logging.info(f'Quality: {quality}, Size:{size/1024}KB')

            if size/1024 <=target_size or quality < MIN_QUALITY:
                break

            quality -=10
    except Exception as e:
        logging.error(e)

    return file_out,get_size(file_out)

if __name__ == '__main__':
    conpress_image('computer_kuan_201632_18.jpg',target_size=1024)