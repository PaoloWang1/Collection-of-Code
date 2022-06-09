def select_min(alist):
    minimum = alist[0]
    for x in range(1, len(alist)):
        if alist[x] < minimum:
            miniumum = alist[x]
    alist[0] = miniumum
    return alist
            
