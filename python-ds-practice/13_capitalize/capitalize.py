def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    x = phrase[:1]
    y = phrase[1:]
    print(x.upper())
    print(y)
    return x.upper() + y
    