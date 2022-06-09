def int_to_binary(num):
    binary = []
    while num >= 1:
        remainder = num % 2
        if remainder:
            num = num - 1
        binary.append(int(remainder))
        num = num / 2
    return binary[::-1]

print(int_to_binary(13))
