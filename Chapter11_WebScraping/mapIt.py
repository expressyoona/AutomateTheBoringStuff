#Launches a map in the browser using an address from the cmd or clipboard
import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
	#Get address from command line
	address = ' '.join(sys.argv[1:])
	print(address)
else:
#TODO: Get address from clipboard
	address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)
