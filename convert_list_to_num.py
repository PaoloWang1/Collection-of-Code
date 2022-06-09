def convert_list_to_num(digit_list):
    number = 0
    multiplier = 1
    
    if digit_list[0] == "-":
        multiplier *= -1
        digit_list.remove("-")
        
    for x in range(len(digit_list)):
        number+= digit_list[x] * (10 ** (len(digit_list) -x -1))
    number *= multiplier
    
    return(number)
