#!/usr/bin/python3
for x in range(0, 26):
    print('{}'.format(chr(122 - x) if x % 2 == 0 else chr(90 - x)), end='')
