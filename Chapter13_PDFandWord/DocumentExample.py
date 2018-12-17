"""
doc = docx.Document('example.docx')

--- APPYING STYLE ---
doc.paragraphs[0].style = ''

doc.paragraphs[0].runs[1].style = ''
doc.paragraphs[0].runs[1].underline = True
doc.save('des.docx')

--- CREATING ---
doc = docx.Document()
para1 = doc.add_paragraph('First line.', [style = ''])
doc.save('des.docx')

doc.add_paragraph('Third line.')
para1.add_run('\nSecond line.')

--- ADDING HEADING ---
doc.add_heading('Text', 1/2/3/4)

--- ADDING LINE AND PAGE BREAKS ---
doc.add_page_break()

--- ADDING PICTURE ---
doc.add_picture('abc.jpg', [width=Inches(), height=Cm()])
"""
