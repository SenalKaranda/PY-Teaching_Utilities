import pymysql.cursors
from os.path import exists
import os

names = []
versions = []
dir = input("Enter Directory").encode('unicode-escape')
if(os.path.exists(dir)):
    for f in os.listdir(dir):
          names.append(f)
    filename = dir + "FileNamesOutput.txt"
    try:
        with open(filename, 'wb') as f:
            f.write(names)
            f.close()
