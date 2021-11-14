#!/usr/bin/env python3

try:
    f = open('readme.txt')
    for line in f:
        print(line, end = '')
except BaseException as err: #catch-all errors
    print('ERROOR occured:', err)
finally:
    if 'f' in locals() and f:
        f.close()
        
        
try:
    x = 1/0
except ZeroDivisionError as e:
    print(e)    
    


# raise exceptions
def f(x,y):
    if x < 0 or y < 0:
        raise ValueError('only positive parameter')
    else: return x+y
    
try:
    z=f(-1,5)
except ValueError as err:
    print(err)
    