import os
import logging

from PIL import Image

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Image_Resize:
    support_formats = ['png', 'jpg', 'jpeg']

    def __init__(self, quality=75):
        self.quality = quality

    def resize(self, src_file: str, width: int, height: int, dst_file: str = None, mode='min') -> Image:
        if width <= 0 or height <= 0:
            raise ValueError('Width and Height must be positive numbers')

        if not os.path.exists(src_file):
            raise FileNotFoundError

        filename, ext = os.path.splitext(os.path.basename(src_file))
        dst_file = dst_file or f'{filename}_compressed{ext}'
        if ext[1:] not in self.support_formats:
            raise ValueError(f'Unsupported format: {ext}')

        logger.debug('Opening Image %s', src_file)

        with Image.open(src_file) as img:
            origin_w, origin_h = img.size

            logger.debug('Claculating resize ratio')
            ratio= self.get_ratio(origin_w,origin_h,width,height)
            new_size = (int(origin_w * ratio), int(origin_h * ratio))

            logger.debug('Resizing the img to %s',new_size)
            resized_img = img.resize(new_size)

            logger.debug('Saving resized img to %s',dst_file)
            resized_img.save(dst_file, quality=self.quality)

    def get_ratio(self,origin_w,origin_h,width,height,mode):
        return mode(width / origin_w, height / origin_h)

    def mul_resize(self):
        pass

if __name__ == '__main__':
    Image_Resize().resize('',1024,768)
