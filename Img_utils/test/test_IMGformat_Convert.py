import pytest

from Img_utils.IMGformat_Convert import img2Convert, img_folder2Convert


class Test_IMGformat:
    def test_format(self):
        img2Convert('Picture\\1.jpg', 'png')
        img2Convert('Picture\\1.jpg', 'jpeg')
        img2Convert('Picture\\1.jpg', 'bmp')
        img2Convert('Picture\\1.jpg', 'jfif')
        img2Convert('Picture\\1.jpg', 'webp')
        img2Convert('Picture\\1.jpg', 'jpg')

        img2Convert('Picture\\2.jpeg', 'png')
        img2Convert('Picture\\2.jpeg', 'jpeg')
        img2Convert('Picture\\2.jpeg', 'bmp')
        img2Convert('Picture\\2.jpeg', 'jfif')
        img2Convert('Picture\\2.jpeg', 'webp')
        img2Convert('Picture\\2.jpeg', 'jpg')

        img2Convert('Picture\\3.png', 'png')
        img2Convert('Picture\\3.png', 'jpeg')
        img2Convert('Picture\\3.png', 'bmp')
        img2Convert('Picture\\3.png', 'jfif')
        img2Convert('Picture\\3.png', 'webp')
        img2Convert('Picture\\3.png', 'jpg')

        img2Convert('Picture\\9.bmp', 'png')
        img2Convert('Picture\\9.bmp', 'jpeg')
        img2Convert('Picture\\9.bmp', 'bmp')
        img2Convert('Picture\\9.bmp', 'jfif')
        img2Convert('Picture\\9.bmp', 'webp')
        img2Convert('Picture\\9.bmp', 'jpg')



    def test_folderformat(self):
        img_folder2Convert('Picture', 'png')