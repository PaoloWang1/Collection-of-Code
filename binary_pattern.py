def check_pattern(number):
    d = 0
    if number % 2 == 0:
        d = 2
    else:
        d = 1
    while d < number:
        d += d * 2
        d += d * 2
        if d == number:
            return True
    return False

print(check_pattern(21))
