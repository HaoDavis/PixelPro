import pytest

from Img_utils.IMG_Conpress import conpress_image


class Test_IMG_Conpress:
    def test_conpress_image(self):
        conpress_image('Picture\\1.jpg','Picture\\11.jpg',1024)
        conpress_image('Picture\\2.JPEG', 'Picture\\22.JPEG', 1024)
        conpress_image('Picture\\3.png', 'Picture\\33.png', 1024)
        conpress_image('Picture\\4.jpg', 'Picture\\44.jpg', 1024)
        conpress_image('Picture\\5.png', 'Picture\\55.png', 1024)
        conpress_image('Picture\\6.JPEG', 'Picture\\66.JPEG', 1024)
        conpress_image('Picture\\7.gif', 'Picture\\77.gif', 1024)
        conpress_image('Picture\\8.jpg', 'Picture\\88.jpg', 1024)
        conpress_image('Picture\\9.bmp', 'Picture\\99.bmp', 1024)
        with pytest.raises(FileNotFoundError):
            conpress_image('Picture\\1111.png','Picture\\11111.png',1024)

