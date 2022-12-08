def cntn_link(s, elm):
    if not s:
        return False
    elif s[0] == elm:
        return True

    return cntn_link(s[1:], elm)

def empty():
    return []

def link(first, rest):
    return [first, rest]

print(cntn_link (link(1, link(2, link(3, empty()))), 1))
print(cntn_link (link(1, link(2, link(3, empty()))), 4))

