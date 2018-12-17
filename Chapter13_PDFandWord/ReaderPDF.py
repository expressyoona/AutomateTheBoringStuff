import PyPDF2
pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages #Return the page's number of the document.
pageObj = pdfReader.getPage(num)
pageObj.extractText()
"""
pdfReader.isEncrypted -> Kiểm tra file có bị mã hóa bằng pass
pdfReader.decrypt('pass')

--- CREATING PDFs ---
1. Open one/more existing PDFs into PdfFileReader objects.
pdfFile = open('example.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
2. Create a new PdfFileWriter object.
pdfWriter = PyPDF2.PdfFileWriter()
3. Copy page from the PdfFileReader objects into the PdfFileWriter objects.
for pageNum in range(pdfReader.numPages):
	pageObj = pdfReader.getPage(pageNum)
	pdfWriter.addPage(pageObj)
	--> Always add pages to the end.
4. Finally, use the PdfFileWriter object to write the output PDF.
	pdfOutputFile = open('dest.pdf', 'wb')
	pdfWriter.write(pdfOutputFile)
	pdfOutputFile.close()
	pdfFile.close()

--- ROTATING PAGES ---
page = pdfReader.getPage(0)
page.rotateClockwise(90/180/270)
-> Save.

--- OVERLAYING PAGES ---
Insert watermark
page.mergePage(watermark) #Water is also a PDF file.
-> Save.

--- ENCRYPTING PDFs ---
pdfWriter.encrypt('user_password', 'owner_password')
#User password allows you to view the PDF.
#Owner password allows you to set permissions for printing, cmt, extracting text,...


"""
