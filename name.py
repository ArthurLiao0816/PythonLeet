import os
import sys
title = sys.argv[1:]
dirName = ''.join(title)

if not os.path.exists(dirName):
    os.mkdir(dirName)
with open(file=dirName+'/try.py', mode='x'):
    pass

print(title)
print(dirName)
