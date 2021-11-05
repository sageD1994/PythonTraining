#!/usr/bin/env python3
#above Shebang line, sets the location of the interpreter

#import time   ... all functions for timehandling
#       locale ... get local settings
import time, locale

#input reads in entered text
name = input('Geben Sie ihren Namen an: ')
print('Hallo %s!' % name)

#get current Date and Time
#set local language
locale.setlocale(locale.LC_ALL, '')
#sets date and time
time = time.strftime('Heute ist %A, der %d. %B. ')
print(time)