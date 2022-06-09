def gcd(x, y):
    big = max(x, y)
    small = min(x, y)
    r = big % small
    if r == 0:
        return small
    else:
        return gcd(small, r)

print(gcd(12,21))
