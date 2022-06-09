
num1 = 0
def compute_row_values(list1):
    for y in list1:
        num1 = 0
        for x in range(3):
            if list1[y][x] == 1:
                num1 += 1 * (x + 1)
        print (num1)
                
