#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if not (x % 3 == 0 or x % 5 == 0):
            print('{} '.format(x), end='')
        elif x % 3 == 0 and not x % 5 == 0:
            print('{} '.format('Fizz'), end='')
        elif x % 5 == 0 and not x % 3 == 0:
            print('{} '.format('Buzz'), end='')
        elif x % 5 == 0 and x % 3 == 0:
            print('{} '.format('FizzBuzz'), end='')
