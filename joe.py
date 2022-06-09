def create_list(n,m):
    LiSt = []
    num = 0
    for x in range(n):
        LiSt.append([])
    for y in range(m):
        LiSt.append([num])
        num += 1
    print(LiSt)
