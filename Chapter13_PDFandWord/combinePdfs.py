#! Python 3
# combinePdfs.py - Combine all the PDFs in the current working dir
# into a single PDF.
import PyPDF2, os

#Get all the PDF filenames
pdfFiles = []
for filename in os.listdir('.'):
	if filename.endswith('.pdf'):
		pdfFiles.append(filename)
pdfFiles.sort(key = str.lower)
pdfWriter = PyPDF2.PdfFileWriter()
print(pdfFiles)
#TODO: Loop through all the PDFs files.
for filename in pdfFiles:
	pdfFileObj = open(filename, 'rb')
	print(filename)
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
		#TODO: Loop through all the pages(except the first) & add them.
	for pageNum in range(1, pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)
#TODO: Save the resulting PDF to a file.
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
print('Saved!')
