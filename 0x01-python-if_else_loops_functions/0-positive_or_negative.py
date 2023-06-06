#!/usr/bin/python3
import random
number = random.randint(-10, 10)
message = ''
if number > 0:
    message = 'positive'
elif number == 0:
    message = 'zero'
else:
    message = 'negative'
print(f'{number} is {message}')
