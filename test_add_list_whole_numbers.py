import math
import random

N_TESTS = 100
MAX_WHOLE_NUM = 1000000


def convert_num_to_list(num):
    digits = []
    digits_placeholder = num
    counter = 0
    while digits_placeholder / 10 >= 1:
        digits_placeholder = digits_placeholder / 10
        counter+=1
        
    value = 0
    y=num
    for x in range(counter+1):
        value = math.floor(y/(10**(counter-x)))
        digits.append(value)
        y -= value*(10**(counter-x))
    return(digits)
    

def convert_list_to_num(digit_list):
    number = 0
    for x in range(len(digit_list)):
        number+= digit_list[x] * (10 ** (len(digit_list) -x -1))
    return(number)


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
    
    return(sum_list[::-1])


for x in range(N_TESTS):
    n1 = random.randint(0, MAX_WHOLE_NUM)
    n2 = random.randint(0, MAX_WHOLE_NUM)

    returned = convert_list_to_num(add_list_whole_numbers(convert_num_to_list(n1),
                                      convert_num_to_list(n2)))

    if returned == n1+n2:
        print("check")
    else:
        print(n1, n2, returned, n1+n2, "WRONG")
        break
    
    
