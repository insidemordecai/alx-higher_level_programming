#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    lastdigit = number % 10
else:
    lastdigit = ((number * -1) % 10) * -1

output = 'Last digit of {} is {} and is'.format(number, lastdigit)

if lastdigit == 0:
    print(output, '0')
elif lastdigit > 5:
    print(output, 'greater than 5')
else:
    print(output, 'less than 6 and not 0')
