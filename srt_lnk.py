# //check if linked list is sorted?

def srt(lnk):
    if not lnk:
        return True
    elif not lnk[1]:
        return True
    elif lnk[0] > lnk[1][0]:
        return False
    else:
        return srt(lnk[1])

def empty():
    return []

def link(first, rest):
    return [first, rest]



lnk1 = link(1, link(2, link(3, link(4, empty()))))
print(srt(lnk1))

lnk2 = link(1, link(3, link(2, link(4, link(5, empty())))))
print(srt(lnk2))

lnk3 = link(3, link(3, link(3, empty())))
print(srt (lnk3))
   
