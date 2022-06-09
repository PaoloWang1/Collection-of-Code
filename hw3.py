def listf(row, column):
    m = []
    count = 0
    for x in range(row):
        m.append([])
        for y in range(column):
            m[x].append(count)
            count+=1
    return m
