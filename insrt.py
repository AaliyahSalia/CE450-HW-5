def insrt(l, elm, ind):
    if ind == 0:
        return link(elm, l)
    elif not l:
        return link(elm, empty())
    else:
        return link(first(l), insrt(rest(l), elm, ind - 1))

def empty():
    return []

def first(lnk):
    return lnk[0]

def rest(lnk):
    return lnk[1]

def link(first, rest):
    return [first, rest]

l = link(11, link(12, link(13, empty())))
n = insrt (l, 2021, 1)
print(n)

m = insrt(n, 2022, 20)
print(m)

