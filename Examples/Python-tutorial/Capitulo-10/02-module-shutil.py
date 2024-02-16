#!/usr/bin/env python3

import shutil
shutil.copyfile('test/data1.txt', 'test/data2.txt')

shutil.move('test/data2.txt', 'test/data3.txt')
