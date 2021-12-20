#!/usr/bin/python3.8
import os, platform

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def convert_type(size_in_bytes, size_type):
    """ Convert the size from bytes to other types like KB, MB or GB"""
    if size_type == "BYTES":
        return size_in_bytes
    elif size_type == "KB":
        return size_in_bytes / 1024
    elif size_type == "MB":
        return size_in_bytes / (1024*1024)
    elif size_type == "GB":
        return size_in_bytes / (1024*1024*1024)
    else:
        print("Please give you the correct type")

def get_file_size(file_name, size_type):
    """ Get file in size in given unit like KB, MB or GB"""
    size = os.path.getsize(file_name)
    return convert_type(size, size_type)

def get_files_list(directory_name):
    files = []
    for r,d,f in os.walk(directory_name):
        for each_file in f:
            files.append(os.path.join(r,each_file))
    return files

def main():
    clear()



if __name__ == '__main__':
    main()

