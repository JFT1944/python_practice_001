def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    z = []
    q = phrase.split( )
    print(q)
    for p in q:
        f = p[:1]
        r = p[1:]
        y = f.upper() + r.lower()
        z.append(y)
    a = " "[:].join(z)    
    print(a)
    print(z)
    return a
titleize('oNLy cAPITALIZe fIRSt')