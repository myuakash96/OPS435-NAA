#!/usr/bin/env python3
# Author ID: myuakash
def read_file_string(file_name):
    # Takes a filename string, returns a string of all lines in the file

    f = open(file_name,'r')
    file_string = f.read()
    f.close()
    return file_string

def read_file_list(file_name):
    # Takes a filename string, returns a list of lines without new-line characters

    f = open(file_name,'r')
    file_list = f.readlines()
    f.close()
    result = []
    for i in file_list:
        result.append(i.strip())

    return result

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
