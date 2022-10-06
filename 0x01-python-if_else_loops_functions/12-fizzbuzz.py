#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        print('{}'.format(x if not (x % 3 == 0 or x % 5 == 0) else ''), end=' ')
        print('{}'.format('fizz' if (x % 3 == 0 and not(x % 5 == 0)) else ''), end=' ')
        print('{}'.format('buzz' if (x % 5 == 0 and not(x % 3 == 0)) else ''), end=' ')
        print('{}'.format('fizzbuzz' if (x % 5 == 0 and x % 3 == 0) else ''), end=' ')
