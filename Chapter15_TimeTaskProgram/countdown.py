#A simple countdown script.
#Win 10: subprocess.Popen(['start', 'filename'], shell=True) -> Open a file with default application.
import time, subprocess
timeLeft = 10
while timeLeft > 0:
	print(timeLeft, end='')
	time.sleep(1)
	timeLeft -= 1
#TODO: At the end of the countdown, play a sound file.
subprocess.Popen(['start', 'alarm.wav'], shell=True)
