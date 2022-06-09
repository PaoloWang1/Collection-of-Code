def parse_str():
    string1 = input("Enter some text")
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    number = ""
    list_num = []
    for letters in range(len(string1)):
        if string1[letters] == "-" and letters < len(string1)-1 and string1[letters+1] in nums and len(number) == 0:
            number += string1[letters]
        elif string1[letters] in nums:
            number += string1[letters]
        elif len(number) != 0:
            list_num.append(int(number))
            number = ""
    list_num.append(int(number))
    return list_num

print(parse_str())
