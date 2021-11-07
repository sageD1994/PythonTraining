#!/usr/bin/env python3

# decimal to calc without rounderror
import decimal as dec

#float
a=0.7
b=0.9
c=a+0.1
d=b-0.1

print ('Usign float:', c==d, c-d)

# decimal
a = dec.Decimal('0.7')
b = dec.Decimal('0.9')
c = a + dec.Decimal('0.1')
d = b - dec.Decimal('0.1')

print ('Usign dezimal:', c==d, c-d)
