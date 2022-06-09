letters = {}
string = "an elephant is in the house"
string = list(string)
for x in range(len(string)):
    if string[x] in letters:
        letters[string[x]] += 1
    else:
        letters[string[x]] = 1

sorted_letters = sorted(letters)
for x in range(len(letters)):
    print(sorted_letters[x] + " : " + str(letters[sorted_letters[x]]))
