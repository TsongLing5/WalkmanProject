#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os


def getFile(path):
    print("Get pic fileName")
    # path = os.getcwd()  # 文件夹目录
    print(path)
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    # print(files)
    # print(type(files))
    PEFList = []

    for name in files:
        if os.path.isdir(path + '/' + name):
            # print(path +name)
            PEFList.extend(getFile(path + '/' + name))  # 回调函数，对所有子文件夹进行搜索
        elif os.path.isfile(path + '/' + name):
            # print(type(format))
            # print(type(name))
            if ('flac' in name.lower() or 'mp3' in name.lower() or 'wav' in name.lower() or 'wmv' in name.lower()):
                PEFList.append(path + '/' + name)
                # print(PEFList)
            # while("PEF" not in name):
            #     pass
        else:
            print("未知文件:%s", name)

    # print(PEFList)
    return PEFList


path = os.getcwd()  # 文件夹目录
list = getFile(path)
print("Over")

file = open('WalkmanPC.txt')
deleteList = open('DeleteList.txt', 'w')
con = file.readlines()
print(len(con))
# for pc in con:
for walkman in list:
    count = 0
    for pc in con:
        if (walkman.split("/")[-1] in pc):
            break
        count = count + 1
    if (count == len(con)):
        deleteList.write(walkman + '\n')

deleteList.close()

# for n in list:
#     file.write(n+'\n')
file.close()
