#!/usr/bin/env python3

#get sum of numbers 1 to x
x = int(input('Sum of numbers 1 to ... '))

sumGau = (x*(x+1))/2
print('With gauß:', sumGau)

#for
sumFor = 0
for i in range(1,x+1,1):
    sumFor += i
print('With for:', sumFor)

#while
sumWhile = 0
i = 1
while i <= x:
    sumWhile += i
    i += 1
print('With while:', sumWhile)
