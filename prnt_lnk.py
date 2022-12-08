#Create a function to print linked list as follows.

def prnt_lnk(s):
    if not s:
        return
    print(s[0])
    return prnt_lnk(s[1])

def empty():
    return []

def link(first, rest):
    return [first, rest]


print(prnt_lnk(link(1, link(2, link(3, link(4, empty()))))))

