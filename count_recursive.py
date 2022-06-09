def binary_to_decimal(binary_num):
    print("input argument: ", binary_num)
    if len(binary_num) == 0:
        return 0
    result = int(binary_num[-1])
    return_value = binary_to_decimal(binary_num[:-1])
    result += return_value * 2

    return result
print(binary_to_decimal("1101"))
