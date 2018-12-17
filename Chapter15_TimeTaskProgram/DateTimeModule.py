"""

--- TIME ---
import time
now = time.time()
-> Return the total seconds since 1/1/1970
time.sleep(k)
round(now[, k])

--- DATETIME ---
datetime.datetime.now() #datetime.datetime(2018, 9, 11, 9, 22, 3, 412312)
dt = datetime.datetime(year, month, day[, hour, minute, second])
datetime.datetime.fromtimestamp(k) k is second unit
date1 > date2 True if date1 later than date2
delta = datetime.timedelta(days = d, hours = h, minutes = m, seconds = s)
delta.total_seconds()

--- CONVERTING DATETIME INTO STRINGS ---

dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
dt.strftime('')
	%Y: 2015
	%y: year(00 - 99)
	%m: month(1 - 12)
	%B: January - December
	%b: Jan - Dec
	%d: day(01 - 31)
	%j: Day of the year(001 - 366)
	%w: Day of the week(0/Sunday - 6/Saturday)
	%A: Full weekday name(Monday - Sunday)
	%a: Mon - Sun
	%H: hour(0 - 23)
	%I: hour(01 - 12)
	%M: minute(00 - 59)
	%S: second(00 - 59)
	%p: 'AM' or 'PM'

--- CONVERTING STRINGS INTO DATETIME ---
Using datetime.datetime.strptime('String', 'format')
"""
