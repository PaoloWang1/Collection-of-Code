def stairs(c, b):
    g = []
    if c <= 1:
        return 1
    '''
    s1 = stairs(c-2)
    s2 = stairs(c-1)
    '''
    if b > c:
        b = c
    for x in range(b):
        g.append(stairs(c-x, b))
    return sum(g)

print(stairs(3, 2))

