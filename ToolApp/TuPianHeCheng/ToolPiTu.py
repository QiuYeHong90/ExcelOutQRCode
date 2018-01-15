#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '
from PIL import Image
import os
__author__ = '袁书辉'


def PiTuFuntion(imgpath,index,outPath):
    # 加载底图
    base_img = Image.open(ur'/Users/zhao/Desktop/work/webServerPhp/ToolApp/ToolApp/TuPianHeCheng/bg.png')
    # 可以查看图片的size和mode，常见mode有RGB和RGBA，RGBA比RGB多了Alpha透明度
    # print base_img.size, base_img.mode
    box = (1168, 92,1168+327,92+327)  # 底图上需要P掉的区域

    # 加载需要P上去的图片 ur'/Users/zhao/Desktop/work/webServerPhp/ToolApp/ToolApp/TuPianHeCheng/5元代金券201.jpg'
    tmp_img = Image.open(imgpath)
    # 这里可以选择一块区域或者整张图片
    # region = tmp_img.crop((0,0,304,546)) #选择一块区域
    # 或者使用整张图片
    region = tmp_img

    # 使用 paste(region, box) 方法将图片粘贴到另一种图片上去.
    # 注意，region的大小必须和box的大小完全匹配。但是两张图片的mode可以不同，合并的时候回自动转化。如果需要保留透明度，则使用RGMA mode
    # 提前将图片进行缩放，以适应box区域大小
    # region = region.rotate(180) #对图片进行旋转
    print  box
    region = region.resize((box[2] - box[0], box[3] - box[1]))

    base_img.paste(region, box)
    # base_img.show() # 查看合成的图片
    base_img.save(outPath+str(index)+'out.png')  # 保存图片


# PiTuFuntion()


def PiTuFuntionFileName(path,outPath):
    i=0
    for filename in os.listdir(path):  # listdir的参数是文件夹的路径
         #此时的filename是文件夹中文件的名称
        newPath = path+filename
        print (newPath)
        PiTuFuntion(newPath,i,outPath)
        i+=1

# PiTuFuntionFileName("/Users/zhao/Desktop/work/webServerPhp/ToolApp/ToolApp/TuPianHeCheng/abcd/",'/Users/zhao/Desktop/work/webServerPhp/ToolApp/ToolApp/TuPianHeCheng/out/')
