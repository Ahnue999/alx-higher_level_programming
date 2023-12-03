def add_tuple(tuple_a=(), tuple_b=()):
    alen = len(tuple_a)
    blen = len(tuple_b)
    if alen < 2:
        if alen == 0:
            a1, a2 = 0, 0
        else:
            a1, a2 = tuple_a[0], 0
    else:
        a1, a2 = tuple_a[0], tuple_a[1]
    if blen < 2:
        if blen == 0:
            b1, b2 = 0, 0
        else:
            b1, b2 = tuple_b[0], 0
    else:
        b1, b2 = tuple_b[0], tuple_b[1]

    sum = ((a1 + b1), (a2 + b2))
    return sum
