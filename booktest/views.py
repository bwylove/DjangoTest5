#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from models import *
from django.core.paginator import *

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

# 用于做分页
def herolist(request,pindex):
    if pindex=='':
        pindex='1'
    list=HeroInfo.objects.all()
    paginator=Paginator(list,5)
    page=paginator.page(int(pindex))
    context={'page':page}
    return render(request,'booktest/herolist.html',context)

#进行分页练习
def herolist(request,pindex):
    list=HeroInfo.objects.all()
    paginator=Paginator(list,5)
    page=paginator.page(int(pindex))
    context={'page':page}
    return render(request,'booktest/herolist.html',context)

#省市区选择
def area(request):
    return render(request,'booktest/area.html')
def pro(request):
    prolist=AreaInfo.objects.filter(parea__isnull=True)
    list=[]
    for area in prolist:
        list.append([area.id,area.title])
    return JsonResponse({'data':list})

def city(request,id):
    citylist=AreaInfo.objects.filter(parea_id=id)
    list=[]
    for item in citylist:
        list.append({'id':item.id,'title':item.title})
    return JsonResponse({'data':list})