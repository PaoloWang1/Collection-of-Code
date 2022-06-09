def is_palindrome(x):
    x = list(x)
    reversed = ""
    length = len(x)
    for z in range(length):
        if not str(x[z-1]).isalpha():
            x.remove(x[z-1])
    reversed = x[::-1]
    print(reversed)
    if reversed == x:
        return True
    else:
        return False

    
