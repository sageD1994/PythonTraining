#!/usr/bin/env python3

d = {'red' : 0xff0000, 'green' : 0xff00, 'blue' : 0xff}
print(d)
print(d['red'])
print(hex(d['red']))

print(d.get('orange'))

#add elemets
d['black'] = 0
#remove
del d ['red']
print(d)

print(d.values())
print(d.keys())

for f in d:
    print('The colour', f, 'has the code', hex(d[f]))