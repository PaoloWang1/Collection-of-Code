with open("cs03p_ciphered_text.txt", "r") as file:
    lines = file.readlines()
lines = str(lines)
list_form = []
keep_going = ""


while not keep_going:
    list_form = []
    for x in range(len(lines)):
        list_form.append(chr(ord(lines[x])+1))
    print("".join(list_form))
    lines = ("".join(list_form))
    keep_going = input()
