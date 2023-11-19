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
| 戴子豪 | 编写博客 Scrum 冲刺 1 及 Scrum 冲刺集合贴、组织站立会议、绘制项目燃尽图。  | 编写博客 Scrum 冲刺 2 及 更新 Scrum 冲刺集合贴、组织站立会议、绘制项目燃尽图。 | 成员在时间上很难凑齐，讨论积极性欠缺。 |
| 朱俊荣 | Django代码框架学习与初步搭建。 | 考虑如何将图片文件从前端接收与返回渲染。 | 许多代码与操作流程跟网上的教程有很大出入。 |
| 李铭伟 | 初步完成格式转换功能  | 修复完善代码  | 第一次细致地学习 Pillow 库 |
| 陈倚星 | 构思图片裁剪的实现代码形成大体的思路 | 初步实现图片裁剪的代码。 | 不知道如何实现按任意方式调节大小。在网上找了很多资料，明天再完善一下。 |
| 卫宇琪 | 初步完成图片文字识别功能，制订功能实现、GUI界面以及代码测试计划。 | 进行界面开发和代码测试。 | 第一次深入接触界面开发库，经验不足。 |
| 张震 | 制订测试计划，选择测试方法。 | 完善方案。 | 难以在众多测试方法间进行取舍，不知道许多测试方法的具体适用场景。 |
| 甫尔达吾斯 | 初步实现照片换底色的功能。 | 查找漏洞，修复完善。 | 第一次接触这方面的工作，发现自己对很多不足，还需继续努力。 |

# 项目燃尽图
![image](https://img2023.cnblogs.com/blog/3270285/202311/3270285-20231119092537981-132385731.png)

# 签入记录
## 代码/文档签入记录
![image](https://img2023.cnblogs.com/blog/3270285/202311/3270285-20231119085134426-1377395120.png)
## 对应的 Issue 内容与链接
| 成员 | Issue 内容与链接 |
|:----:|:---:|
| 戴子豪 | [团队博客](https://github.com/HaoDavis/PixelPro/issues/13) |
| 朱俊荣 | [Django代码框架](https://github.com/HaoDavis/PixelPro/issues/3) |
| 李铭伟 | [图片格式转换](https://github.com/HaoDavis/PixelPro/issues/12) |
| 陈倚星 | [图片裁剪](https://github.com/HaoDavis/PixelPro/issues/4) |
| 卫宇琪 | [图片文字识别](https://github.com/HaoDavis/PixelPro/issues/11) |
| 张震 | [功能测试](https://github.com/HaoDavis/PixelPro/issues/14) |
| 甫尔达吾斯 | [证件照换底色](https://github.com/HaoDavis/PixelPro/issues/6) |
## Code Review 编码规范文档状态
无变化
# 项目进度
## 部分模块代码
```python
import os

from PIL import Image
from svglib.svglib import svg2rlg

# 图片格式支持：  png jpg bmp
# TODO :  webp svg
path_in = r'data'
path_out = r'result'

# 单次与多次
def imgConvert(path_in,target_format):
    """
    param path_in: 原图片路径
    :param target_format:  图片输出格式
    :return bool：是否成功
    """
    Dir_img = path_in.split('.')[0]
    format_list = ['.jpg', '.png', '.jpeg', '.webp', '.bmp', '.tiff']
    with Image.open(path_in) as source_img:
        src_format = source_img.format
        src_mode = source_img.mode
        if src_format != target_format:
            source_img = source_img.convert('RGB')  # 将源图像convert到PIL支持的mode
            target_img = Image.new(src_mode, source_img.size)  # 创建目标对象
            target_img.putdata(list(source_img.getdata()))  # 将像素从源图像复制到目标图像
            file_name = f'{Dir_img}.{target_format}'
            target_img.save(file_name)
            print('Convert to {} successfully'.format(target_format))
        else:
            print('formats are the same,no need to convert 😅')





if __name__ == '__main__' :
    imgConvert('data/img.png','jpg')
```
## 部分运行结果
![image](https://img2023.cnblogs.com/blog/3270285/202311/3270285-20231119093435554-185785000.png)

# 总结
| 成员 | 总结 |
|:----:|:---:|
| 戴子豪 | 团队协作耗时较长、实际编写代码只是一小部分 |
| 朱俊荣 | 很多问题网上都难以直接找到解决办法，需要自己思考 |
| 李铭伟 | 多学习多思考 |
| 陈倚星 | 多构思，遇到不懂多上网。 |
| 卫宇琪 | 参考前辈的经验和总结，边学习边进步。 |
| 张震 | 查阅资料，向有经验的人请教。 |
| 甫尔达吾斯 | 更加巩固关于这方面的知识，提高代码完成能力。 |