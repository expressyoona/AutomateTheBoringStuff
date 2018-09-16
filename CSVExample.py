"""
--- STEP BY STEP---
1. Open file:
exampleFile = open('example.csv')
2. Read file:
exampleReader = csv.reader(exampleFile)
3. Get data:
exampleData = list(exampleReader)
exampleData[0][0]

--- WRITER OBJECTS ---
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow([a, b, c, d])
"""
import csv
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
"""
for row in exampleData:
	for col in row:
		print(col, end = ' ')
	print()
"""
for row in exampleReader:
	print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
print('DONE!')	
