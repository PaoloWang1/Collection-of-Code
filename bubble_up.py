def bubble_up(alist):
    elem = 0
    for index in range(len(alist)-1):
        if alist[index] < alist[index+1]:
            elem = alist[index]
            alist[index] = alist[index+1]
            alist[index+1] = elem
    return alist


def select_min(lis):
    length = len(lis)
    for index in range(len(lis),-1,-1):
        lis[:index] = bubble_up(lis[:index])
    return lis

bubble_up([3,2,1])
