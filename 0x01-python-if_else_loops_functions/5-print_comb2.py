n range(0, 100):
    if x == 99:
        print('{:2d}'.format(x))
    else:
        print('{:02d}'.format(x), end=', ')
