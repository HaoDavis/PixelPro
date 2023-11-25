import os
from PIL import Image
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from glob import glob
import logging

logging.basicConfig(filename='compress.log', level=logging.DEBUG)

MIN_QUALITY = 20

def get_size(filename):
    return os.path.getsize(filename)

def conpress_image(file_in, file_out=None, target_size=1500):
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

    logging.info(f'Compressing {file_in} to {file_out}')

    try:
        quality = 50
        while True:
            with Image.open(file_in) as img:
                img.save(file_out, quality=quality)

            size = get_size(file_out)
            logging.info(f'Quality: {quality}, Size:{size/1024}KB')

            if size/1024 <= target_size or quality < MIN_QUALITY:
                break

            quality -= 10
    except Exception as e:
        logging.error(e)

    return file_out, get_size(file_out)

def compress_image(input_image_path, output_image_path):
    fileType = input_image_path.split(".")[-1]
    with Image.open(input_image_path) as image:
        image.save(output_image_path, fileType.upper(), optimize=True, quality=1)

def img2Convert(path_in, target_format):
    Dir_img, src_format = os.path.splitext(path_in)
    if src_format.lower() == '.svg':
        drawing = svg2rlg(path_in)
        renderPM.drawToFile(drawing, Dir_img+'.'+target_format, fmt=target_format.upper())
    with Image.open(path_in) as source_img:
        src_mode = source_img.mode
        if src_format.lower() != '.' + target_format.lower():
            source_img = source_img.convert('RGB')
            target_img = Image.new(src_mode, source_img.size)
            target_img.putdata(list(source_img.getdata()))
            file_name = f'{Dir_img}.{target_format}'
            target_img.save(file_name)
            print(f'Convert {path_in} to {target_format} successfully')
        else:
            print(f'Formats are the same, no need to convert {path_in} 😅')

def img_folder2Convert(file_folder, tgt_format):
    for img in glob(file_folder + '/*'):
        img_format = os.path.splitext(img)[1][1:].upper()
        if img_format not in ['PNG', 'JPG', 'BMP', 'SVG', 'JFIF', 'WEBP']:
            print(f'The format of {img} is not supported yet')
        else:
            img2Convert(img, tgt_format)

keyToFunc = {
    'compress_image': compress_image,
    'conpress_image': conpress_image,
    'img_folder2Convert': img_folder2Convert
}

if __name__ == '__main__':
    conpress_image('computer_kuan_201632_18.jpg', target_size=1024)
    img_folder2Convert('data', 'PNG')  # 作为示例调用
