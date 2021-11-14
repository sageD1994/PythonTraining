#!/usr/bin/env python3

#normal function
def fiblist(n):
    a,b = 0,1
    result = []
    for _ in range(n):
        result += [a]
        a, b = b, a+b
    return result

print(fiblist(10))


#generator
def fibgen(n):
    a, b = 0,1
    for _ in range(n):
        yield a
        a,b = b, a+b
        
        
print(fibgen(10))
print(list(fibgen(10)))
      
      
gen = fibgen(20)
fib = next(gen)
      
while fib<10000: 
    print(fib, end = '   ')
    fib = next(gen, None)
    if fib == None:
        print('Generator erschöpft')
        break
