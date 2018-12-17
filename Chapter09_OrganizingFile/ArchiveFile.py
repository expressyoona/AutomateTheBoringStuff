import zipfile, os
os.chdir('E:\\')
exampleZip = zipfile.ZipFile('example.zip')
print(exampleZip.namelist())
#Return a list of strings for all the files and folders contained in the ZIP file.
spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))
exampleZip.extractall(path)
#Extract the zip file into path. Default, path is current folder.
exampleZip.extract(file, path)
#extract a single file from the ZIP file.
"""
newZip = zipfile.ZipFile('new.zip', 'w')
#w = overide, a = append
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
--> Create a new ZIP file named new.zip that has the compressed contents of spam.txt
"""
exampleZip.close()
