def change(lnk, u, v):
    if not lnk:
        return []
    elif lnk[0] == u:
        return link(v, change(lnk[1], u, v))
    else:
        return link(lnk[0], change(lnk[1], u, v))

def empty():
    return []

def link(first, rest):
    return [first, rest]

l = link(1, link(2, link(3, empty())))
n = change(l, 3, 1)
print(n)

m = change(n, 1, 2)
print(m)

print(change(m, 5, 1))

