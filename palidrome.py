def palidrome(word):
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return palidrome(word[1:-1])
    else:
        return False

print(palidrome("abba"))
