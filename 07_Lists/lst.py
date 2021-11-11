#!/usr/bin/env Python3

lst = [1, 2.3, 'abc', 'efg', 12]

print(lst[2])
print(lst[2:4])
print(lst[::-1])

lst = list(range(10,100,10))
print(lst)

print([x*2+1 for x in lst])
for x in lst:
    print(x, x*x, x**3, sep='\t')
    
print(len(lst))
lst.extend([110]) # at the end
lst.insert(5,55) # at pos 5

print(lst)

lst.pop(5)
print(lst)

lst += [120, 130]
print(lst)

del lst[-3:]
print(lst)

lst.remove(80)
print(lst)
