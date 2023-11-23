import pytest

from Img_utils.IMG_Resize import Image_Resize


class Test_IMG_Resize:
    def test_IMG_Resize(self):
        Image_Resize().resize('Picture\\1.jpg',1280,720)
        Image_Resize().resize('Picture\\2.jpeg', 1920, 1080)
        Image_Resize().resize('Picture\\3.png', 1280, 960)
        Image_Resize().resize('Picture\\4.jpg', 1024, 768)
        Image_Resize().resize('Picture\\5.png', 1440, 900)
        Image_Resize().resize('Picture\\6.jpeg', 800, 600)
        with pytest.raises(ValueError):
            Image_Resize().resize('Picture\\7.gif', 800, 600)
        with pytest.raises(FileNotFoundError):
            Image_Resize().resize('Picture\\1111.jpg', 800, 600)
        with pytest.raises(ValueError):
            Image_Resize().resize('Picture\\1.jpg', -800, -600)