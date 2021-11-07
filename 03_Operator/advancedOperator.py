#!/usr/bin/env python3


#diference between == and is
a = 'abc'
b = 'abc'

print("a = 'abc'", "b = 'abc'", sep=', ')

if a==b:
    print('The content of a and b are the same')
if a is b:
    print('a and b reference on the same object')

#list
a = ['a', 'b', 'c']
b = ['a']
b.append('b')
b.append('c')

print(a,b)
if a==b:
    print('The content of a and b are the same')
if a is b:
    print('a and b reference on the same object')

