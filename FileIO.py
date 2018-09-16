import os
os.path.join('user', 'bin', 'spam')
#Trả về đường dẫn thư mục hiện tại
os.getcwd()
#Thay đổi đường dẫn, path là string và path phải là 1 thư mục
os.chdir(path)
#Tạo thư mục
os.makedir(path)
#os.makedirs('C:\\delicious\\walnut\\waffles')
#Convert from relative path to absolute path
os.path.abspath(path)

os.path.isabs(path)
#True if path is absolute path.
os.path.dirname(path)
#Return the parent's path
os.basename(path)
#Return the base name follows the last backslash in a path
os.path.getsize(path)
#Return size of path(byte)
os.listdir(path)
#<=> DIRectory
os.path.exists(path)
os.path.isfile(path)
os.path.isdir(path)