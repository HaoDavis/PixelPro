import os
import logging

from PIL import Image


def Image_Resize(src_file, width, height,dst_file=None, quality=75):
    """
    param src_file: Source file path
    :param dst_file: Destination file path
    :param width: Output width
    :param height: Output height
    :param quality: JPEG quality from 0-100
    """
    if width <= 0 or height <= 0:
        raise ValueError('Width and Height must be positive numbers')

    if not os.path.exists(src_file):
        raise FileNotFoundError

    basename, ext = os.path.splitext(os.path.basename(src_file))
    dst_file = dst_file or f'{basename}_compressed{ext}'

    logging.info(f'Resize {src_file} to {dst_file}')

    try:
        with Image.open(src_file) as img:
            origin_w, origin_h = img.size
            
            logging.info(f'Original size: {origin_w}*{origin_h}')
            ratio = min(width / origin_w, height / origin_h)
            new_size = (int(origin_w * ratio), int(origin_h * ratio))

            resized_img = img.resize(new_size)
            resized_img.save(dst_file,quality=quality)
    except Exception as e:
        logging.error(f'Failed to resized image:{e} ')
        raise e

if __name__ == '__main__':
    Image_Resize('computer_kuan_201632_18.jpg',1024,768)