#!/usr/bin/env python3

s='Hello World!'

#inverted
print(s[::-1])

name = 'Dave'
age  = 27

#%
print('%s is %d years old' % (name,age))
print('1/7 with 3 decimals: %.3f' % (1/7))

#format
print('{a} is {b} years old'.format(a=name,b=age))
print('1/7 with 3 decimals: {:.3f}'.format(1/7))

#short format
x=1/7
print(f'{name} is {age} years old')
print(f'{x:.2}')