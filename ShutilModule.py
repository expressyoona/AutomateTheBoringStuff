import shutil, os
shutil.copy(src, des)/move(src, des)
#Used to copy a file
#src and des are strings. If des is a filename, it will be used as the new name of the copied file.
shutil.copytree(src, des)
#Used to copy a folder
os.unlink(path)
#Delete the file at path
os.rmdir(path)
#Delete the folder at path. This folder must be empty of any files or folders.
shutil.rmtree(path)
#Remove the folder at path. Also delete all files and folders it contains.