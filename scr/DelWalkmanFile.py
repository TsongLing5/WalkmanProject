#!/usr/bin/python
# -*- coding: UTF-8 -*-
from builtins import input
import os


def deleteFile(path):
    if(os.path.isdir(path)):
        pass
    else:
        os.remove(path)

def getPic(path):
    print("Get pic fileName")
    #path = os.getcwd()  # 文件夹目录
    print(path)
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    print(files)
    # print(type(files))
    PEFList = []

    for name in files:
        if os.path.isdir(path +'/'+name):
            # print(path +name)
            PEFList.extend(getPic(path +'/'+name)) #回调函数，对所有子文件夹进行搜索
        elif os.path.isfile(path +'/'+name):
            # print(type(format))
            # print(type(name))
            if ('flac' in name.lower() or 'mp3' in name.lower() or 'wav' in name.lower() or 'wmv' in name.lower()):
                PEFList.append(path +'/'+ name)
                # print(PEFList)
            # while("PEF" not in name):
            #     pass
        else:
            print("未知文件:%s",name)

    print(PEFList)
    return PEFList

def SyncPC2Walkman():
   file=open('DeleteList.txt')
   deleteList=file.readlines()
   for item in deleteList:
       deleteFile(item)

def deleteEmptyFolder():
    path = os.getcwd()  # 文件夹目录
    files = os.listdir(path)  # 获取路径下的子文件(夹)列表
    for file in files:
        print 'Traversal at', file
        if(os.path.isdir(file)):  # 如果是文件夹
            if(not os.listdir(file)):  # 如果子文件为空
                os.rmdir(file)  # 删除这个空文件夹


str = input("Enter your input: ")
if(str=="123456"):
    print("Received input is : ", str)
    SyncPC2Walkman()
    deleteEmptyFolder()
else:
    print('SN ERROR!')