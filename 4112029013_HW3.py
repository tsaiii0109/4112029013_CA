# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 00:00:00 2023

@author: User
"""

import os
import time
import shutil

os.mkdir('CS')

os.makedirs('homework')

with open('homework/homework.txt', 'w') as file:
  file.write('4112029013_陳采均\n')

with open('homework/homework.txt', 'r') as file:  
    content=file.read()
    print(f'\n檔案內容:{content}')

file_size = os.path.getsize('homework/homework.txt')
print(f'文件大小: {file_size}字節')

modification_time = os.path.getmtime('homework/homework.txt')
print(f'最後修改時間: {modification_time}')

formatted_time = time.ctime(modification_time)
print(f'最後修改時間 (人類可讀格式): {formatted_time}')

#僅刪除檔案
#os.remove('homework/homework.txt')

#刪除整個非空目錄
shutil.rmtree('homework')

#刪除空目錄
os.rmdir('CS')
print('已删除目录: CS')