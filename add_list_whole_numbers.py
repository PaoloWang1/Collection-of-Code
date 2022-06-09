def add_list_whole_numbers(digit_list1, digit_list2):
    digit_list1 = digit_list1[::-1]
    digit_list2 = digit_list2[::-1]

    in_order_list = []
    sum_list = []

    if len(digit_list1) >= len(digit_list2):
        in_order_list.append(digit_list1)
        in_order_list.append(digit_list2)
    else:
        in_order_list.append(digit_list2)
        in_order_list.append(digit_list1)

    for x in range(len(in_order_list[1])):
        sum_list.append(digit_list1[x] + digit_list2[x])

    for x in range(len(in_order_list[0]) - len(in_order_list[1])):
        sum_list.append(in_order_list[0][x + len(in_order_list[1])])
      
    for x in range(len(sum_list)):
        if sum_list[x] > 9:
            if x == len(sum_list)-1:
                sum_list.append(0)
            sum_list[x] -= 10
            sum_list[x+1] += 1
            
    return(sum_list[::-1])
