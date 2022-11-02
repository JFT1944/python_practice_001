def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    # fin = []
    # while (len(phrase) * -1) < count:
    #      print count
    #      count -=1
    farray = []
    for x in phrase:
        farray.insert(0, x)
    print(phrase.split())
    print(farray)
    print ("".join(farray))
    return ("".join(farray))


reverse_string('awesome')