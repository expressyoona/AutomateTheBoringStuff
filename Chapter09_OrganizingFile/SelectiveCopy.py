import os, shutil
def CopySpecific(folder):
	folder = os.path.abspath(folder) #Convert to absolute path
	des = 'F:\\Backup'
	for foldername, subfolders, filenames in os.walk(folder):
		#print(subfolders)
		for i in range(len(subfolders)):
			print(subfolders[i])
		for filename in filenames:
			if filename.endswith('.html'):
				pass
				"""
				Check information before copy
				#print(filename)
				#print(os.path.join(foldername, filename))
				#shutil.copy(os.path.join(foldername, filename), des)
				"""
	print('Done!')
CopySpecific('F:\\IT\\Web')
