def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    arr = []
    for p in phrase:
        if p == to_swap:
           arr.append(p.swapcase())
        elif p == to_swap.upper():
            arr.append(p.swapcase())
        elif p == to_swap.lower():
            arr.append(p.swapcase())
        else:
            arr.append(p)
    print("".join(arr))
