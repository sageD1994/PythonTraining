#!/usr/bin/env python3

#input reads in entered text
year = int(input('Geben Sie ein Jahr an: '))

if year % 400 == 0:
    schaltjahr = True
elif year % 100 == 0:
    schaltjahr = False
elif year % 4 == 0:
    schaltjahr = True
else: schaltjahr = False

if schaltjahr: print(year, 'ist ein schaltjahr')
else:          print(year, 'ist kein schaltjahr')