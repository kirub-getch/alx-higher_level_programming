#!/usr/bin/python3
for letter in range(97, 123):
    if not (chr(letter) == 'e' or chr(letter) == 'q'):
        print('{}'.format(chr(letter)), end='')
