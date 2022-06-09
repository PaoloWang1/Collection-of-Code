string1 = "hello world"
string2 = "something"
length = len(string1)
length2 = len(string2)
printed = ""
for times in range(0, length):
    for times2 in range(0, length2):
        if string1[times] == string2[times2]:
            printed += string1[1]
            
print(set(printed))
