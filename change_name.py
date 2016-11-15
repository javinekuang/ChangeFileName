# coding=utf-8
import sys
import os
import codecs

helpString = "add number for your filename like this filename_1.png\n" \
             "  -h --- for help\n" \
             "  -d --- source file dir\n" \
             "  -a --- add number\n" \
             "  -c --- clear number\n\n"


# find the files and change their name
def change_name(file_dir, is_add):
    sep_dot = "."
    sep_line = "_"
    filenames = os.listdir(file_dir)
    index = 0
    if is_add:
        for f in filenames:
            index += 1
            file_path = file_dir+"\\"+f
            items = f.split(sep_dot)
            items[-2] = items[-2]+sep_line+str(index)
            new_path = file_dir + "\\" + sep_dot.join(items)
            print new_path
            os.rename(file_path, new_path)
    else:
        for f in filenames:
            file_path = file_dir + "\\" + f
            items = f.split(sep_dot)
            temps = items[-2].split(sep_line)
            items[-2] = sep_line.join(temps[:-1])
            new_path = file_dir + "\\"
            new_path += sep_dot.join(items)
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
    change_name(file_dir, is_add)
    return


def main():
    if len(sys.argv) < 2:
        print "err:No action specified"
    else:
        deal_actions()
    return

main()


