def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    phr = ""
    for x in range(num):
        print(phrase)
        phr = phr+phrase
    print(phr)    
    return(phr)
repeat('ay', 4)