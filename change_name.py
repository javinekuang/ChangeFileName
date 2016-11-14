# coding=utf-8
import sys
import os
import codecs

helpString = "修改文件名，给文件名添加序号：\n" \
             "  -h --- for help\n" \
             "  -d --- 目标文件夹目录\n\n" \
             "  -a --- 添加后缀\n" \
             "  -c --- 清除最后的后缀\n\n" \
             "  -m --- 模式设置\n"


# find the files and change their name
def change_name(file_dir, mode, is_add):
    filenames = os.listdir(file_dir)
    index = 0
    if is_add:
        for f in filenames:
            index += 1
            file_path = file_dir+"\\"+f
            items = f.split(".")
            new_path = file_dir+"\\" + items[-2]+"_"+str(index)+"."+items[-1]
            print new_path
            os.rename(file_path, new_path)
    else:
        for f in filenames:
            file_path = file_dir + "\\" + f
            items = f.split(".")
            temps = items[0].split("_")
            length = len(temps)
            new_path = file_dir + "\\"
            for i in range(length):
                if i != length - 1:
                    new_path += temps[i]
                if i < length - 2:
                    new_path += "_"
            new_path += "."+items[-1]
            os.rename(file_path, new_path)
    return


# deal the input args
def deal_actions():
    file_dir = ""
    mode = 0
    is_add = True
    for index in range(len(sys.argv)):
        arg = sys.argv[index]
        if arg.__eq__("-h"):
            print helpString
            quit()
        elif arg.__eq__("-d"):
            file_dir = sys.argv[index+1]
        elif arg.__eq__("-m"):
            mode = 1
        elif arg.__eq__("-a"):
            is_add = True
        elif arg.__eq__("-c"):
            is_add = False
    change_name(file_dir, mode, is_add)
    return


def main():
    if len(sys.argv) < 2:
        print "err:No action specified"
    else:
        deal_actions()
    return

main()


