def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase.strip()
    print (phrase)
    l1 = []
    l2 = []
    for p in phrase:
        if p == " ":
          print('space')
        else:
          l1.append(p)
          l2.insert(0, p)
    if l1 == l2:
      return True
    else:
      return "yo this shit ain't a palindrome"
