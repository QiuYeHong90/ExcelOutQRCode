#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

from TuPianHeCheng import ToolPiTu

from django.shortcuts import render
import time
from datetime import datetime

from ToolApp.settings import BASE_DIR
from zip import ZipUtilities

from ToolQRCode import QRCode
import shutil
import os
from django.http import HttpResponse, StreamingHttpResponse

__author__ = '袁书辉'



def index(request):

    print request.get_host()
    homeUrl = 'http://'+request.get_host();
    return render(request, 'index.html',{"homeUrl":homeUrl})



def upload_file(request):
    print '来了'
    homeUrl = 'http://'+request.get_host();

    timeStr = str(time.time())
    excelpath = os.path.join(BASE_DIR, "ToolApp/uploadExcel/"+timeStr)
    outQrcodeimgPath =  os.path.join(BASE_DIR, 'static/qrcodeImg/'+timeStr)
    outPiTuImgPath =  os.path.join(BASE_DIR, 'static/PiTu/'+timeStr)

    imgUrlPath = 'static/qrcodeImg/'+timeStr;

    # 输出的zip路径
    outZipPath1 = 'static/QrcodeZip/'+timeStr

    outZipPath =  os.path.join(BASE_DIR, outZipPath1)
    zipUrlPath = homeUrl+outZipPath1



    if request.method == "POST":    # 请求方法为POST时，进行处理
        print 'post哈哈'
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        makeDirPath(excelpath)
        destination = open(os.path.join(excelpath,myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()

        makeDirPath(outQrcodeimgPath)
        makeDirPath(outPiTuImgPath)



        List = QRCode.main(os.path.join(excelpath,myFile.name),outQrcodeimgPath)

        ToolPiTu.PiTuFuntionFileName(outQrcodeimgPath+'/',outPiTuImgPath+'/')

        makeDirPath(outZipPath)
        ziUrl = zipUrlPath+ZipUtilities.adddirfile(outQrcodeimgPath+'/',outZipPath)
        print  List,ziUrl


        return render(request, 'Qrcode.html',{'List': List,"homeUrl":ziUrl})
    else:

        print 'get'
        return render(request, 'uploadExcel.html')

def upload_filePitu(request):
    print '来了'
    homeUrl = 'http://'+request.get_host()+'/';

    timeStr = str(time.time())
    excelpath = os.path.join(BASE_DIR, "ToolApp/uploadExcel/"+timeStr)
    outQrcodeimgPath =  os.path.join(BASE_DIR, 'static/qrcodeImg/'+timeStr)
    outPiTuImgPath =  os.path.join(BASE_DIR, 'static/PiTu/'+timeStr)

    imgUrlPath = 'static/qrcodeImg/'+timeStr;

    # 输出的zip路径
    outZipPath1 = 'static/PiTuZip/'+timeStr

    outZipPath =  os.path.join(BASE_DIR, outZipPath1)
    zipUrlPath = homeUrl+outZipPath1

    print zipUrlPath


    if request.method == "POST":    # 请求方法为POST时，进行处理
        print 'post哈哈'
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        makeDirPath(excelpath)
        destination = open(os.path.join(excelpath,myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()

        makeDirPath(outQrcodeimgPath)
        makeDirPath(outPiTuImgPath)



        List = QRCode.main(os.path.join(excelpath,myFile.name),outQrcodeimgPath)

        print  outPiTuImgPath
        ToolPiTu.PiTuFuntionFileName(outQrcodeimgPath+'/',outPiTuImgPath+'/')

        makeDirPath(outZipPath)
        ziUrl = zipUrlPath+ZipUtilities.adddirfile(outPiTuImgPath+'/',outZipPath)
        print  List,ziUrl


        return render(request, 'Qrcode.html',{'List': List,"homeUrl":ziUrl})
    else:

        print 'get'
        return render(request, 'uploadExcelOutYouHuiQuan.html')




def makeDirPath(outQrcodeimgPath):
    print  outQrcodeimgPath
    if os.path.exists(outQrcodeimgPath):
        #只能删除空目录
        shutil.rmtree(outQrcodeimgPath) #空目录、有内容的目录都可以删
        os.rmdir(outQrcodeimgPath)
    os.mkdir(outQrcodeimgPath)
    print "目录已创建"




def add(request):
    if request.method == "POST":
        a = request.POST['a']
        b = request.POST['b']
        c = request.POST['c']
        print a + c + b


        if a=='':
            a = 0
        else:
            a = int(a)
        if b == '':
            b = 0
        else:
            b = int(b)


        if c=='+':
            r=a+b
        elif c=='-':
            r = a - b
        elif c == '*':
            r = a * b
        else:
            r = a / b

        rStr = str(a)+str(c)+str(b)+'='+str(r)
        print  rStr
        return render(request, 'JiSuanQi.html',{'r':rStr})

    return render(request, 'JiSuanQi.html',{'r':0})

