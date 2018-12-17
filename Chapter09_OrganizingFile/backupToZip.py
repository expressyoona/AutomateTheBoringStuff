import zipfile, os
def backupToZip(folder):
	#Backup the entire contents of 'folder' into a ZIP file.
	folder = os.path.abspath(folder)
	#Figure out the filename this code should use based on
	#what files already exist
	number = 1
	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFilename):
			break
		number += 1
	#TODO: Create the ZIP file.
	print('Creating %s...' % (zipFilename))
	backupZip = zipfile.ZipFile(zipFilename, 'w')
	#TODO: Walk the entire folder tree and compress the files in each folder.
	for foldername, subfolders, filenames in os.walk(folder):
		print('Adding file in %s...' % (foldername))
		#Add the current folder to the ZIP files.
		backupZip.write(foldername)
		#Add all the files in this folder to the ZIP file.
		for filename in filenames:
			newBase = os.path.basename(folder) + '_'
			if filename.startswith(newBase) and filename.endswith('.zip'):
				continue #Don't backup the backup zip files
			backupZip.write(os.path.join(foldername, filename))
	backupZip.close()
	print('Done.')
backupToZip('C:\\delicious')
