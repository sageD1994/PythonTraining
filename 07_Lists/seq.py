#!/usr/bin/env python3


#seqences can not change (e.g. no remove/add elements like in lists)

t = (12, 73, 3)
print(t)
print(t[0])
print(t[1:3])

from random import randint
n = randint(1,20)
print(n)
if n in (2,3,5,7,11,13,17,19):
    print('Prim %d' % n)
    
print ((1,2,3)<(1,2,3))
print ((1,2,3)<(2,2,3))
print ((1,2,3)<(2,2))

lst1=list(range(1,11))
lst2=list('abcdefghij')
print(list(zip(lst1,lst2)))