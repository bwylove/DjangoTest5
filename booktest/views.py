# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'booktest/index.html')
# 文件上传
def uploadPic(request):
    return render(request,'booktest/uploadPic.html')
def uploadHandle(request):
    pic1=request.FILES['pic1']
    picName=os.path.join(settings.MEDIA_ROOT,pic1.name)
    with open(picName,'w') as pic:
        for c in pic1.chunks():
            pic.write(c)
    return HttpResponse('<img src="/static/media/%s" />'%pic1.name)
