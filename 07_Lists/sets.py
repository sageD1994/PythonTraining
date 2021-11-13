#!/usr/bin/env python3


#  sets can only use hashable objects
s= {1,2, 3}
print(s)
s = set('Hello World!')
print(s)

#add elements
s.add('x')
print('H' in s)

#remove
s.remove('H')
s.clear()
print(s)


x = set('abcdef')
y = set('efgh')

print('Vereinigung: ', x|y)
print('Differenz: ', x-y)
print('Schnittmenge: ', x&y)
print('XOR: ', x^y)