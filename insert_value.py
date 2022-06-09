def insert_value(alist, value):
    for x in range(len(alist)):
        if value < alist[x]:
            alist.insert(x, value)
            break
    return(alist)
