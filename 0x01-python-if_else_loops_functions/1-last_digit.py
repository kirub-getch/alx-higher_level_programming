#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit: int = -1 * (10 - number % 10)
print(f'Last digit of {number:d} is {digit:d}', end=' ')
if digit > 5:
    print(f'and is greater than 5')
elif digit == 0:
    print(f"and is 0")
elif digit < 6 and not 0:
    print(f"and is less than 6 and not 0")
