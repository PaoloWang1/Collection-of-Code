import random
def insert_value(alist, value):
    length = len(alist)
    for x in range(len(alist)):
        if value < alist[x]:
            alist.insert(x, value)
            break
        
    if len(alist) == length:
        alist.append(value)
    return(alist)

def insertion_sort(alist):
    for x in range(len(alist)-1):
         sorted_list = insert_value(alist[:x+1], alist[x+1])
         behind_list = alist[x+2:]
         alist = sorted_list
         
         for x in range(len(behind_list)):
             alist.append(behind_list[x])
    return(alist)

def test_code():
    MAXIMUM_NUMBERS = 100
    empty = []
    
    for x in range(100):
        empty = []
        for x in range(MAXIMUM_NUMBERS):
            empty.append(random.randint(0,9))
        if insertion_sort(empty) == sorted(empty):
            print("check")
        else:
            print("wrong", empty, insertion_sort(empty), sorted(empty))
            break
