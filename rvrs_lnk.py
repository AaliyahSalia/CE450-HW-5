def rvrs_lnk(s):
    rvrs = []
    while s:
        rvrs = link(s[0], rvrs)
        s = s[1]
    return rvrs

def print_list(s):
    while s:
        print(s[0])
        s = s[1]
    print()

def empty():
    return []

def link(first, rest):
    return [first, rest]

print(rvrs_lnk(link(1, link(2, link(3, link(4, empty()))))))
