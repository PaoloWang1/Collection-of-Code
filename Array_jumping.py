def array_jumping(list1):
    d = 0
    stack = [0]
    list2 = [len(list1) - 1]
    while len(stack) > 0:
        stack = []
        for x in range(len(list1)):
            for y in range(len(list2)):
                if x + list1[x] >= list2[y]:
                    if d < 1:
                        stack.append(x)
                        print(list2, stack, x, y, list1, 2)
                        break
                    elif x < y:
                        stack.append(x)
                        print(list2, stack, x, y, list1, 1)
                        break
        if 0 in stack:
            return True
        if len(stack) == 0:
            return False
        stack = set(stack)
        stack = list(stack)
        list2 = []
        for g in stack:
            list2.append(list1[g])
        d+=1
        print(d)
    return True

print(array_jumping([2,3,1,1,4]))
