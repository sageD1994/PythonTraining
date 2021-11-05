#!/usr/bin/env python3

# print options:
#  sep   ... seperator                     standard ' '
#  end   ... end of string                 standard '\n'
#  file  ... set where the output will be    

#sep
print(1, 2, 3)
print(1, 2, 3, sep = '---')

#end
print(1, 2, 3, sep=';', end='.\nEOF\n')

f = open('out.txt', 'w')
print(1, 2, 3, file=f)
f.close()