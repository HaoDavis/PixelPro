| 这个作业属于哪个课程 | [软件工程](https://edu.cnblogs.com/campus/gdgy/CSGrade21-12) |
| :-----------------: |:---------------: |
| 这个作业要求在哪里 | [团队作业4——项目冲刺](https://edu.cnblogs.com/campus/gdgy/CSGrade21-12/homework/13020) |
| 这个作业的目标 | 记录昨日已完成工作，明确今日工作，总结项目进度 |

# 敏捷冲刺日志集合
[项目冲刺集合贴](https://www.cnblogs.com/notingblogs/p/17840948.html)

# 站立会议
## 会议照片
因每个人不单有软工项目，在线下时间上凑齐所有人较为困难，所以我们采用微信会议的方式进行。
![image](https://img2023.cnblogs.com/blog/3270285/202311/3270285-20231119081324179-2117685492.png)

## 会议内容
| 成员 | 昨日完成 | 今日计划 | 遇到的困难 |
|:----:|:---:|:------------:|:---------:|
| 戴子豪 | 编写博客 Scrum 冲刺 5 及 Scrum 冲刺集合贴、组织站立会议、绘制项目燃尽图。  | 编写博客 Scrum 冲刺 6 及 更新 Scrum 冲刺集合贴、组织站立会议、绘制项目燃尽图。 | 成员在时间上很难凑齐，讨论积极性欠缺。 |
| 朱俊荣 | 解决图像前端显示失真问题 。 | post请求优化。 | 显示在前端页面的图像变形失真。 |
| 李铭伟 | 测试模块。| 继续测试  | 测试流程的不连贯。 |
| 陈倚星 | 图片裁剪的代码完成，不过比较简单 | 解决图片读取问题。 | 图片读取有点问题。 |
| 卫宇琪 | OCR的代码完成，环境搭建成功。 | 对部分单元进行测试，进行代码维护。 | 部分依赖项存在版本冲突。 |
| 张震 | 完成了对两个模块的单元测试。 | 总结问题。 | 环境配置以及单元测试完全覆盖。 |
| 甫尔达吾斯 | 代码测试。 | 测试。 | 不断出现漏洞，代码还需要测试。 |

# 项目燃尽图
![image](https://img2023.cnblogs.com/blog/3270285/202311/3270285-20231123125527127-2023074014.png)

# 签入记录
## 代码/文档签入记录
![image](https://img2023.cnblogs.com/blog/3270285/202311/3270285-20231123125538282-1364899680.png)

## 对应的 Issue 内容与链接
| 成员 | Issue 内容与链接 |
|:----:|:---:|
| 戴子豪 | [团队博客](https://github.com/HaoDavis/PixelPro/issues/13) |
| 朱俊荣 | [整体结合](https://github.com/HaoDavis/PixelPro/issues/14) |
| 李铭伟 | [各功能完善](https://github.com/HaoDavis/PixelPro/issues/8) |
| 陈倚星 | [自由大小裁剪](https://github.com/HaoDavis/PixelPro/issues/4) |
| 卫宇琪 | [图片文字识别](https://github.com/HaoDavis/PixelPro/issues/11) |
| 张震 | [功能测试](https://github.com/HaoDavis/PixelPro/issues/14) |
| 甫尔达吾斯 | [证件照换底色](https://github.com/HaoDavis/PixelPro/issues/6) |
## Code Review 编码规范文档状态
无变化
# 项目进度
## 部分模块代码
文字识别：
```python
import argparse
import codecs
import logging
import os
import os.path as osp
import sys
from guiocr import __appname__
from guiocr.app import MainWindow
from guiocr.utils import newIcon
from PyQt5 import QtCore, QtGui, QtWidgets


def main():
    QtCore.QCoreApplication.setOrganizationDomain("casia")
    QtCore.QCoreApplication.setApplicationName(__appname__)
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName(__appname__)
    # app.setWindowIcon(newIcon("icon"))
    win = MainWindow()
    # win = createWindow(win,'blue')

    win.show()
    win.raise_()
    sys.exit(app.exec_())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
```
图片调整大小的改动：
```python
from PIL import Image

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

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
class Image_Resize:
    support_formats = ['png', 'jpg', 'jpeg']

    if not os.path.exists(src_file):
        raise FileNotFoundError
    def __init__(self, quality=75):
        self.quality = quality

    basename, ext = os.path.splitext(os.path.basename(src_file))
    dst_file = dst_file or f'{basename}_compressed{ext}'
    def resize(self, src_file: str, width: int, height: int, dst_file: str = None, mode='min') -> Image:
        if width <= 0 or height <= 0:
            raise ValueError('Width and Height must be positive numbers')

    logging.info(f'Resize {src_file} to {dst_file}')
        if not os.path.exists(src_file):
            raise FileNotFoundError

        filename, ext = os.path.splitext(os.path.basename(src_file))
        dst_file = dst_file or f'{filename}_compressed{ext}'
        if ext[1:] not in self.support_formats:
            raise ValueError(f'Unsupported format: {ext}')

        logger.debug('Opening Image %s', src_file)

    try:
        with Image.open(src_file) as img:
            origin_w, origin_h = img.size
            
            logging.info(f'Original size: {origin_w}*{origin_h}')
            ratio = min(width / origin_w, height / origin_h)

            logger.debug('Claculating resize ratio')
            ratio= self.get_ratio(origin_w,origin_h,width,height)
            new_size = (int(origin_w * ratio), int(origin_h * ratio))

            logger.debug('Resizing the img to %s',new_size)
            resized_img = img.resize(new_size)
            resized_img.save(dst_file,quality=quality)
    except Exception as e:
        logging.error(f'Failed to resized image:{e} ')
        raise e

            logger.debug('Saving resized img to %s',dst_file)
            resized_img.save(dst_file, quality=self.quality)

    def get_ratio(self,origin_w,origin_h,width,height,mode):
        return mode(width / origin_w, height / origin_h)

    def mul_resize(self):
        pass

if __name__ == '__main__':
    Image_Resize('computer_kuan_201632_18.jpg',1024,768)
    Image_Resize().resize('',1024,768)
```
## 部分运行结果
![image](https://img2023.cnblogs.com/blog/3270285/202311/3270285-20231122130341614-1338921857.png)

# 总结
| 成员 | 总结 |
|:----:|:---:|
| 戴子豪 | 团队协作耗时较长、实际编写代码只是一小部分。 |
| 朱俊荣 | 总有意料之外的情况，要耐心应对。 |
| 李铭伟 | 还需要多多学习。 |
| 陈倚星 | 一种方法不行试试另一种。 |
| 卫宇琪 | 关关难过关关过。 |
| 张震 | 仔细检查，耐心完成每一步操作。 |
| 甫尔达吾斯 | 还需要继续完善。 |