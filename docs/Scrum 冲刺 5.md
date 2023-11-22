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
| 戴子豪 | 编写博客 Scrum 冲刺 4 及 Scrum 冲刺集合贴、组织站立会议、绘制项目燃尽图。  | 编写博客 Scrum 冲刺 5 及 更新 Scrum 冲刺集合贴、组织站立会议、绘制项目燃尽图。 | 成员在时间上很难凑齐，讨论积极性欠缺。 |
| 朱俊荣 | 修复框架中.jpg格式的储存问题、将压缩图像功能加入到框架中。 | 将格式转换功能加入到框架中 。 | 涉及路径问题，业务函数接口与框架接口差异问题 。 |
| 李铭伟 | 初步完成所有分配任务   | 尝试扩展  | 没有充分交流。 |
| 陈倚星 | 完成了图片指定大小的裁剪 | 将裁剪扩展到自由大小。 | 实现既定的功能没有那么简单。 |
| 卫宇琪 | 初步完成代码。 | 整体结合测试。 | GUI界面显示异常。 |
| 张震 | 完善结构。 | 继续学习。 | 未经过实际检验。 |
| 甫尔达吾斯 | 整体代码初步完成。 | 测试。 | 很多疑难杂症自己无法完成。 |

# 项目燃尽图
![image](https://img2023.cnblogs.com/blog/3270285/202311/3270285-20231122124730707-589440912.png)

# 签入记录
## 代码/文档签入记录
![image](https://img2023.cnblogs.com/blog/3270285/202311/3270285-20231122124658014-889279927.png)

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
函数测试：
```python
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
```
## 部分运行结果
![image](https://img2023.cnblogs.com/blog/3270285/202311/3270285-20231122130341614-1338921857.png)

# 总结
| 成员 | 总结 |
|:----:|:---:|
| 戴子豪 | 团队协作耗时较长、实际编写代码只是一小部分。 |
| 朱俊荣 | 要充分交流 统一接口提高效率。 |
| 李铭伟 | 需要充分交流。 |
| 陈倚星 | 可以循序渐进，由易到难。 |
| 卫宇琪 | 加油快做好了。 |
| 张震 | 尝试使用过后做出调整。 |
| 甫尔达吾斯 | 还需继续努力。 |