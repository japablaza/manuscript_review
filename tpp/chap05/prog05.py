#!/usr/bin/env python3

import random
import string
import os


def random_string():
    """Testing this finction"""
    x = random.randint(2, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=x))


print('Random text:', random_string())

rey = '/tmp/test1/rey.txt'
file1 = '/tmp/test1/text.md'
path = '/tmp/test1/textfile.txt'
ospath = os.path.dirname(path)
osbasename = os.path.basename(path)
osexist = os.path.isfile(file1)

# print('File directory: ', ospath)
# print('File name: ', osbasename)
# print(file1, 'Exist? ', osexist)

fileopen = open(path).read()
print(fileopen)

if os.path.isfile(rey):
    open(rey)
    print(open(rey).read().upper())
