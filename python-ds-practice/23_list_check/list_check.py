def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for l in lst:
        print (type(l))
        if type(l) == type('str'):
            return False
        
    return True
    