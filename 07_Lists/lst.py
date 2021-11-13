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


#map to apply funktions on all elements of an iterable objects
def quad(x):
    return x*x

lst = [1, 2, 3, 4, 5]
iterator = list(map(quad, lst))
print(iterator)

print([x**3 for x in lst])

lst1 = [7, 1, 4]
lst2 = [10, 11, 21]

def f (x,y):
    return x+y

lst3 = list(map(f, lst1, lst2))
print (lst3)

lst3.sort()
print(lst3)