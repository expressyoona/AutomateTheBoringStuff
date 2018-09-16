import os
"""
os.walk trả về 3 giá trị
1. Một chuỗi là tên thư mục hiện tại.
2. Một list chuỗi chứa thư mục có trong thư mục hiện tại.
3. Một list chuỗi chứa tệp tin trong thư mục hiện tại.
"""
for folderName, subfolders, filenames in os.walk('F:\\IT\\Python'):
	print('The current folder is ' + folderName)
	for subfolder in subfolders:
		print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
	for filename in filenames:
		print('FILE INSIDE ' + folderName + ': ' + filename)
	print()