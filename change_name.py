# coding=utf-8
import sys
import os
import codecs

helpString = "add number for your filename like this filename_1.png：\n" \
             "  -h --- for help\n" \
             "  -d --- source file dir\n\n" \
             "  -a --- add number\n" \
             "  -c --- clear number\n\n"


# 在文件名末尾添加 _num 标记
def append_name_by_dot(items, slap, index):
    length = len(items)
    new_path = ""
    for i in range(length):
        if i == length - 2:
            items[i] += slap + str(index)
        if i != length - 1:
            new_path += items[i] + "."
    new_path += items[-1]
    return new_path


# find the files and change their name
def change_name(file_dir, mode, is_add):
    filenames = os.listdir(file_dir)
    index = 0
    if is_add:
        for f in filenames:
            index += 1
            file_path = file_dir+"\\"+f
            items = f.split(".")
            new_path = file_dir + "\\" + append_name_by_dot(items, "_", index)
            print new_path
            os.rename(file_path, new_path)
    else:
        for f in filenames:
            file_path = file_dir + "\\" + f
            items = f.split(".")
            temps = items[-2].split("_")
            length = len(temps)
            new_path = file_dir + "\\"
            lastname = ""
            for i in range(length):
                if i != length - 1:
                    lastname += temps[i]
                if i < length - 2:
                    lastname += "_"
            items[-2] = lastname
            new_path += append_name_by_dot(items, "", "")
            print new_path
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


