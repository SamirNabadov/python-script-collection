#!/usr/bin/python3.8
import os

def is_file_empty(file_path):
    """ Check if file is empty by confirming if its size is 0 bytes"""
    # Check if file exist and it is empty
    return os.path.exists(file_path) and os.stat(file_path).st_size == 0

def is_file_empty_2(file_name):
    """ Check if file is empty by confirming if its size is 0 bytes"""
    # Check if file exist and it is empty
    return os.path.isfile(file_name) and os.path.getsize(file_name) == 0

def is_file_empty_3(file_name):
    """ Check if file is empty by reading first character in it"""
    # open ile in read mode
    with open(file_name, 'r') as read_obj:
        # read first character
        one_char = read_obj.read(1)
        # if not fetched then file is empty
        if not one_char:
           return True
    return False

def main():
    print('*** Check if file is empty using os.stat() in Python ***')
    file_path = 'E:\\samir\\devops\\python\\scripts\\kube.sh'
    # check if size of file is 0
    if os.stat(file_path).st_size == 0:
        print('File is empty')
    else:
        print('File is not empty')
    
    print('*** Check if file exist and its empty using os.stat() in Python ***')
    file_path = 'E:\\samir\\devops\\python\\scripts\\kube.sh'
    # check if file exist and it is empty
    is_empty = is_file_empty(file_path)
    if is_empty:
        print('File is empty')
    else:
        print('File is not empty')
    
    print('*** Check if file is empty using os.path.getsize() in Python ***')
    file_path = 'E:\\samir\\devops\\python\\scripts\\kube.sh'
    # check if size of file is 0
    if os.path.getsize(file_path) == 0:
        print('File is empty')
    else:
        print('File is not empty')
    
    print('Check if file exist and its empty using os.path.getsize() in Python')
    file_path = 'E:\\samir\\devops\\python\\scripts\\kube.sh'
    # check if file exist and it is empty
    is_empty = is_file_empty_2(file_path)
    if is_empty:
        print('File is empty')
    else:
        print('File is not empty')
    
    print('Check if file is empty by opening and it and reading its first character in Python')
    file_path = 'E:\\samir\\devops\\python\\scripts\\kube.sh'
    # check if file is empty
    is_empty = is_file_empty_3(file_path)
    print(is_empty)
    
if __name__ == '__main__':
   main()
