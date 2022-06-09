def subtract_digit_list(digit_list1, digit_list2): 
    difference_list = []
    greatest_first = []
     
    
    if len(digit_list1) > len(digit_list2):
        for x in range(len(digit_list1) - len(digit_list2)):
            digit_list2.insert(0,0)
    elif len(digit_list2) > len(digit_list1):
        for x in range(len(digit_list2) - len(digit_list1)):
            digit_list1.insert(0,0)

    for x in range(len(digit_list1)):
        if digit_list1[x] > digit_list2[x]:
            greatest_first.append(digit_list1)
            greatest_first.append(digit_list2)
            break
        elif digit_list2[x] > digit_list1[x]:
            greatest_first.append(digit_list2)
            greatest_first.append(digit_list1)
            break

    digit_list1 = greatest_first[0][::-1]
    digit_list2 = greatest_first[1][::-1]
    
    for x in range(len(digit_list2)):
        difference_list.append(digit_list1[x] - digit_list2[x])

    for x in range(len(difference_list)):
        if difference_list[x] < 0:
            difference_list[x] += 10
            difference_list[x+1] -= 1

    difference_list = difference_list[::-1]
    if difference_list[0] == 0:
        difference_list.remove(0)

    return difference_list
