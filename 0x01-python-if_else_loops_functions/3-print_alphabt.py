#!/usr/bin/python3
for i in 'abcdefghijklmnopqrstuvwxyz':
    if not (chr(i) == 'q' or chr(i) == 'e'):
        print('{}'.format(chr(i)), end='')
