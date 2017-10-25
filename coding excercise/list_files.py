#!/usr/bin/python3
import os

def filesizelist():
    for file in os.listdir(os.getcwd()):
        finfo = os.stat(file)
        print("file: {}, size: {} bytes".format(file, finfo.st_size))

if __name__ == '__main__':
    filesizelist()