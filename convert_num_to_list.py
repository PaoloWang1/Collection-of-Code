import math

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
    
