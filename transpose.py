def matrix_transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 
