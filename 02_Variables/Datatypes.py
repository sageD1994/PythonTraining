#!/usr/bin/env python3

#no constant vairables in python

#Datatyps
x=3
print('int: x=3: %s' % x)

x=3.0
print('float: x=3.0: %s' % x)

x=3+4j
print('complex: x=3+4j: %s' % x )

x=bool(1)
print('bool: x=bool(1): %s' % x )

x='abc'
print("str: x='abc': %s" % x )

x=(1,2,3)
print('tupel: x=(1, 2, 3) x[0]: %s' % x[0])

x=[1,2,3]
print('list: x=[1, 2, 3]: %s' % x )

x={1, 2, 3}
print("set: x={1, 2, 3}: %s" % x )

x={1:'red', 2:'blue'}
print("dict: x={1:'red', 2:'blue'}: %s" % x )

#get type of var
print('\n', type(x))

#how to check type
s='abc'
print("s='abc'")
print('isinstance(s,str) = ', isinstance(s,str))
print('isinstance(s,int) = ', isinstance(s,int))