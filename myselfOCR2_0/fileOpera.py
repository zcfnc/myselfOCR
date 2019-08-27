# python3
#  _*_ coding: utf-8 _*_
# _author_ = 'YourName'

import sys
from os import listdir

from numpy import zeros

def writeByteFile(filename, text):
    f = open(filename, 'wb')
    f.write(text)
    f.close()


