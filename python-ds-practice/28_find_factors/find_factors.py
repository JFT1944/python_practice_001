def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    y = []
    for x in range(num + 1):
        # print(x)
        if x == 0:
            print('no')
        elif num % x == 0:
            y.append(x)
        else:
            print('')
    print(y)
find_factors(111)
find_factors(321421)