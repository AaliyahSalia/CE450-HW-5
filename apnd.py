def apnd(lnk, m):
    if not lnk:
        return link(m, empty())
    else:
        return link(lnk[0], apnd(lnk[1], m))

def empty():
    return []

def first(lnk):
    return lnk[0]

def rest(lnk):
    return lnk[1]

def link(first, rest):
    return [first, rest]


l = link(1, link(2, link(3, empty())))
n = apnd (l, 4)
print(n)

print(first(rest(rest(rest(n)))))



