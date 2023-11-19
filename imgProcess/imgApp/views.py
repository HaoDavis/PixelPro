import os

from django.shortcuts import render

# Create your views here.
from imgProcess.settings import BASE_DIR
from utils.imgUtils import keyToFunc
import uuid


def index(request):
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

            func = request.POST.get('func', None)
            if not func:
                msg = "未选择方法"
            if func not in keyToFunc:
                msg = "方法暂不支持"
            else:
                keyToFunc[func](tempPath, factPath)

    return render(request, "index.html", locals())
