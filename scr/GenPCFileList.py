import os

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
path = os.getcwd()  # 文件夹目录
list=getPic(path)
print("Over")

file = open('WalkmanPC.txt','w')
for n in list:
    file.write(n+'\n')
file.close()
