def sum_lnk(lnk, g):
    if not lnk:
        return 0
    else:
        return g(lnk[0]) + sum_lnk(lnk[1], g)

def link(first, rest):
    return [first, rest]

def empty():
    return []

sqr = lambda x: x * x
dbl = lambda y: 2 * y

lnk1 = link(1, link(2, link(3, link(4, empty()))))
print(sum_lnk(lnk1, sqr))

lnk2 = link(3, link(5, link(4, link(6, empty()))))
print(sum_lnk (lnk2, dbl))



