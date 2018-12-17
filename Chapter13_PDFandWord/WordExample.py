"""
--- WORD ---
Module: Python-docx

--- READING WORD DOCUMENTS ---
doc = docx.Document('example.docx')
for i in range(len(doc.paragraphs)):
	print(doc.paragraphs[i].text)
for style in range(len(doc.paragraphs[i].runs)):
	print(doc.paragraphs[1].run[1].text)
"""
