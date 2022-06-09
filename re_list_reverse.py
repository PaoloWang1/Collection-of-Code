def reverse(l):
    if len(l) == 1:
        return [l[0]]
    else:
        return [l.pop()] + reverse(l)


print(reverse([5,3,2,1,4]))
