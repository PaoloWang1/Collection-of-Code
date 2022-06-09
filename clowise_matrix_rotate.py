def rotating_matrix(N):
    editted_list = []
    for cols in range(len(N)):
        row_list = []
        for rows in range(len(N)):
            row_list.append(N[rows][cols])
        editted_list.append(row_list[::-1])
    return(editted_list)

print(rotating_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
