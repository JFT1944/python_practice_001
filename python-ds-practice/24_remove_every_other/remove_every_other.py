lst = [1, 2, 3, 4, 5]
def remove_every_other(lst):

    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    lll = []
    for l in lst:
        if lst.index(l) % 2 == 0:
          lll.append(l)

    print (lll)
    return lll

remove_every_other(lst)