def rotate_matrix(m):
    ret=[]
    for c in range(len(m)):
        ret.append([m[r][c] for r in range(len(m)-1,-1,-1)])
    return ret

print(rotate_matrix([[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]))
