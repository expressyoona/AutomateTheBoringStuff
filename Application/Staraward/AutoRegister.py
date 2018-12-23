#Auto register account
import pyautogui, time, openpyxl

nameField = (459, 228)
exit_bt = (1300, 173)
submit_bt = (651, 637)
signup_bt = (646, 490)
#data = ['account_test', 'daihocdanang', 'daihocdanang', 'Account Test', '01011999', 'id123', '0123456789', 'account@gmail.com']

#Load information's file.
wb = openpyxl.load_workbook('Unregister.xlsx')

sheet = wb.active

row = sheet.max_row

col = sheet.max_column

#First row is header
for i in range(2, row):
	pyautogui.click(nameField[0], nameField[1])
	for j in range(1, col):
		#Fill username, password x 2, fullname, date of birth, ID, phone number and email
		pyautogui.typewrite(str(sheet.cell(row = i, column = j).value) + '\t')
		time.sleep(1)
	#Select province/city
	pyautogui.typewrite(['down', 'down', 'down', '\t'])
	#Select university
	pyautogui.typewrite(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', '\t'])
	#Submit
	pyautogui.click(submit_bt[0], submit_bt[1])
	time.sleep(5)
	#Exit
	pyautogui.click(exit_bt[0], exit_bt[1])
	time.sleep(5)
	#Return
	pyautogui.click(signup_bt[0], signup_bt[1])
	time.sleep(5)

print('Done!')