import threading, time
"""
threadObj = threading.Thread(target = print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
"""
print('Start of program.')

def takeANap():
	time.sleep(5)
	print('Wake up!')

def Hi(s):
	time.sleep(1)
	print('Hello %s' % s)

threadObj = threading.Thread(target = Hi, args=['AI'])
threadObj.start()
threadObj.join()

print('End of program.')
