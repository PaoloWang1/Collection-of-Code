def zigzag(some_str, num_rows):
    img_map = [[] for i in range(num_rows)]
    print(img_map)
    string = ""
    row = 0
    col = 0
    mult = 1
    some_str = list(some_str)
    while len(some_str):
        for x in range(num_rows - 1):
            if len(some_str):
                print(row, len(some_str))
                img_map[row].append(some_str.pop(0))
                row += mult
            else:
                break
        mult *= -1
    return img_map

print(zigzag("helloworld", 4))


#def zigzag(some_str, num_rows):
