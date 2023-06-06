#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
message = ''
if number > 5:
    message = f'{last} and is greater than 5'
elif number == 0:
    message = f'{last} and is 0'
else:
    message = f'-{last} and is less than 6 and not 0'
print(f'Last digit of {number} is {message}')
