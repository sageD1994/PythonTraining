#!/usr/bin/env python3

from datetime import datetime, date, timedelta
import math,  time

now = datetime.now()
print(now)

print(now.isoformat())
print(now.strftime('%A, %d. %B %Y'))

#convert string to date
s = '09-11-2021 18:01'
dt = datetime.strptime(s, '%d-%m-%Y %H:%M')
print(dt.isoformat())

today = date.today()
clock = datetime.now().time()
combine = datetime.combine(today,clock)
print(combine)

#get days till christmas
christmas = date(today.year, 12, 24)
wait = christmas - today
print('Noch', wait.days, '- mal schlafen bis Weihnachten')

#time code
start = time.process_time()

for i in range (1, 10000000):
    x=math.sin(i)

end = time.process_time()
print(end-start, 'Sekunden')
