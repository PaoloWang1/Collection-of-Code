def int_to_binary(num):
    if num == 1:
        return [1]
    b = int_to_binary(num // 2) + [num%2]
    return b

print(int_to_binary(12))
