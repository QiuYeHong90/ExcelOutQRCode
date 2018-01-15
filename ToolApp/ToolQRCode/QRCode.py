
#-*- coding:utf-8 –*-
import xdrlib, sys
import xlrd
import qrcode
from PIL import Image
import os



# 生成二维码 1为29
from ToolApp.settings import BASE_DIR


def makeQRCode(i,url,outPath):
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size = 17,#1为29
        border=2
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    img = img.convert("RGBA")
    icon = Image.open(os.path.join(BASE_DIR, "ToolApp/ToolQRCode/logo.png"))
    img_w, img_h = img.size
    factor = 8
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)

    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    # img.paste(icon, (w, h), icon)
    imgNa ="test"+str(i)+".png"
    img.save( outPath+'/'+imgNa)
    return  imgNa;



# 打开excel

def open_excel(file= '优惠券.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

        print str(e)


#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file='Excel文件路径',colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames =  table.row_values(colnameindex) #某一行数据
    list =[]
    for rownum in range(1,nrows):

         row = table.row_values(rownum)
         if row:
             # app = {}
             # for i in range(len(colnames)):
             #    app[colnames[i]] = row[i]
             list.append(row[0])
    return list
#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file= 'file.xls',colnameindex=0,by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数
    colnames =  table.row_values(colnameindex) #某一行数据
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list

def main(file,outPath):
   tables = excel_table_byindex(file)
   print  "文件的数量"+str(len(tables));
   abc = 0
   list = []
   for row in tables:
       print row
       imgName = makeQRCode(abc,row,outPath)
       print imgName
       list.append(imgName)

       abc+=1;
   return list;


# main()