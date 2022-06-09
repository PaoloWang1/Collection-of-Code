def triangle_matrix(x):
    m = []
    for r in range(x):
        m.append([0]*x)
    for row in range(len(m)):
        for col in range(len(m[row])):
            if row < col:
                m[row][col] = 1
            if row > col:
                m[row][col] = 2
    return m

    
def triange_matrix2(n):
    m = []
    m.append([0]*x) for r in range(x)
