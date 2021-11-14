#!/usr/bin/env python3


day = 6

if day == 1:
    print('Monday')
elif day == 2: print('Tuesday')
elif day == 3: print('Wednesday')
elif day == 4: print('Thursday')
elif day == 5:
    pass  # Todo, code 
elif day == 6:
    print('Saturday')
elif day == 7:
    print('Sunday')

#handle with dict
allDays = {1: 'Monday',2: 'Tuesday', 3:'Wednesday', 4: 'Thursday', 5: 'Friday', 6:'Saturday', 7:'Sunday'}
if day in allDays:
    print(allDays[day])
else: print('unknown')

print('===========================')
print('Print all days except the 4th day')

#for
for i in range(1,8,1): #also possible for i in lists, sets, dict, tuple
    if i == 4: continue #continue to skip this cycle
    if i in allDays: print(allDays[i])
    else: break #stops the loop
else: print("That's all")   #only when all elements in range were looped through, so if a break skips a element it will not be done

#while
i = 1
while i <10000000:
    print(i, end= '   ')
    i += i*i
        