def rotate(string, rotations):
    string = list(string)
    final = ""
    for x in range(len(string)):
        if x == 0:
            nums = sum(rotations)
        else:
            nums = sum(rotations[x::])
        if nums > 27:
            nums = nums % 26
        elif nums < 0:
            nums = 26 - (nums % 26)
        string[x] = ord(string[x]) + nums
        if string[x] < 97:
            string[x] = 123 - (97 - string[x])
        if string[x] > 122:
            string[x] = 96 + string[x] - 122
    for y in string:
        final += chr(y)

    return final

print(rotate("box", [27, 27, 27]))
