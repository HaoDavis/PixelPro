import os

from django.shortcuts import render

# Create your views here.
from imgProcess.settings import BASE_DIR
from utils.imgUtils import keyToFunc
import uuid

keyToName = {
    "compress_image": "压缩图片",
    "getOldImg": "怀旧化处理",
    "oil_effect": "油画处理",
    "img_add": "图片加强",
    "fleet": "流年效果",
    "sketch": "素描效果",
    "resizeImg": "指定大小",
    "convertImg": "格式转换",
    "readText": "文字识别",
    "convertColor": "颜色转换",
}


def index(request, func=None):
    keys = keyToName
    imgName = 'test-img.png'
    if request.method == "POST":
        file = request.FILES.get("img")
        if not file:
            msg = "未选择文件"
        else:
            tempPath = os.path.join(BASE_DIR, 'static', file.name)
            with open(tempPath, 'wb') as f:
                f.write(file.read())
            imgName = f"{uuid.uuid4()}-{file.name}"
            factPath = os.path.join(BASE_DIR, 'static', imgName)
            if not func:
                msg = "未选择方法"
            if func not in keyToFunc:
                msg = "方法暂不支持"
            elif func == 'resizeImg':
                h = int(request.POST.get("height", 400))
                w = int(request.POST.get("weight", 400))
                keyToFunc[func](tempPath, factPath, h, w)
            elif func == 'convertImg':
                target_format = request.POST.get('target_format', 'png')
                factPath = factPath.rsplit(".")[0] + "." + target_format
                keyToFunc[func](tempPath, factPath, target_format)
            elif func == 'convertColor':
                color = request.POST.get('color', 'red')
                keyToFunc[func](tempPath, factPath, color)
            elif func == 'readText':
                text = keyToFunc[func](tempPath)
            else:
                keyToFunc[func](tempPath, factPath)

    return render(request, "index.html", locals())
