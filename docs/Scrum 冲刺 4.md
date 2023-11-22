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
| 戴子豪 | 编写博客 Scrum 冲刺 3 及 Scrum 冲刺集合贴、组织站立会议、绘制项目燃尽图。  | 编写博客 Scrum 冲刺 4 及 更新 Scrum 冲刺集合贴、组织站立会议、绘制项目燃尽图。 | 成员在时间上很难凑齐，讨论积极性欠缺。 |
| 朱俊荣 | 将一个简单的业务业务函数放到框架里测试。 | 完善.jpg格式的处理 。 | 各种格式图片储存方式不同。 |
| 李铭伟 | 压缩图片  | 制定图片大小  | 学习新库、改bug  |
| 陈倚星 | 完成了图片指定大小的裁剪 | 将裁剪扩展到自由大小。 | 代码有少量bug。 |
| 卫宇琪 | 初步完成OCR代码。 | OCR部分整体结合测试。 | 依赖项的环境搭建过程比较坎坷。 |
| 张震 | 完成测试计划。 | 继续学习。 | 测试用例的编写。 |
| 甫尔达吾斯 | 整体代码初步完成。 | 完善结合运行。 | 代码运行还要再去查漏补缺。 |

# 项目燃尽图
![image](https://img2023.cnblogs.com/blog/3270285/202311/3270285-20231121095827878-1291687554.png)

# 签入记录
## 代码/文档签入记录
![image](https://img2023.cnblogs.com/blog/3270285/202311/3270285-20231121095926357-261132955.png)

## 对应的 Issue 内容与链接
| 成员 | Issue 内容与链接 |
|:----:|:---:|
| 戴子豪 | [团队博客](https://github.com/HaoDavis/PixelPro/issues/13) |
| 朱俊荣 | [Django代码框架](https://github.com/HaoDavis/PixelPro/issues/3) |
| 李铭伟 | [图片压缩](https://github.com/HaoDavis/PixelPro/issues/8) |
| 陈倚星 | [图片裁剪](https://github.com/HaoDavis/PixelPro/issues/4) |
| 卫宇琪 | [图片文字识别](https://github.com/HaoDavis/PixelPro/issues/11) |
| 张震 | [功能测试](https://github.com/HaoDavis/PixelPro/issues/14) |
| 甫尔达吾斯 | [证件照换底色](https://github.com/HaoDavis/PixelPro/issues/6) |
## Code Review 编码规范文档状态
无变化
# 项目进度
## 部分模块代码
图片格式转换：
```python
import os

from PIL import Image
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from glob import glob

# 图片格式支持：  png jpg bmp
# TODO :  webp svg
path_in = r'data'
path_out = r'result'
FORMAT = ['PNG', 'JPG', 'BMP', 'SVG', 'JFIF', 'WEBP']


# 单次与多次
def img2Convert(path_in, target_format):
    """
    param path_in: 原图片路径
    :param target_format:  图片输出格式
    :return bool：是否成功
    """
    Dir_img, src_format= path_in.split('.')[0],path_in.split('.')[1]
    if src_format == 'svg':
        drawing = svg2rlg(path_in)
        renderPM.drawToFile(drawing,Dir_img+'.'+target_format,fmt=target_format.upper())
    with Image.open(path_in) as source_img:
        src_mode = source_img.mode
        has_alpha = 'A' in src_mode # bool
        if src_format != target_format:
            source_img = source_img.convert('RGB')  # 将源图像convert到PIL支持的mode
            target_img = Image.new(src_mode, source_img.size)  # 创建目标对象
            target_img.putdata(list(source_img.getdata()))  # 将像素从源图像复制到目标图像
            file_name = f'{Dir_img}.{target_format}'
            target_img.save(file_name)
            print('Convert to {} successfully'.format(target_format))
        else:
            print('formats are the same,no need to convert 😅')


def img_folder2Convert(file_folder, tgt_format):  # 整个文件夹读取图片
    for img in glob(file_folder + '\\*'):
        img_format=img.split('.')[1].upper()
        if img_format not in FORMAT:
            print('the format of {} is not support yet'.format(img))
        else:
            img2Convert(img, tgt_format)
```
图片压缩：
```python
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
```
## 部分运行结果
![image](https://img2023.cnblogs.com/blog/3270285/202311/3270285-20231121100119245-1194377909.png)

# 总结
| 成员 | 总结 |
|:----:|:---:|
| 戴子豪 | 团队协作耗时较长、实际编写代码只是一小部分 |
| 朱俊荣 | 多查阅资料了解原理从而支持应用。 |
| 李铭伟 | 沉淀 |
| 陈倚星 | 可以循序渐进，由易到难。 |
| 卫宇琪 | 继续加油。 |
| 张震 | 继续学习。 |
| 甫尔达吾斯 | 离完成目标还差一点，继续努力。 |