binaryMatrix = [[0, 1, 0, 1, 1],
                [1, 0, 1, 0, 0],
                [0, 0, 0, 1, 0],
                [1, 1, 1, 0, 0],
                [1, 1, 1, 0, 1]]
def largestArea(m):
    num_rows, num_cols = len(m), len(m[0])
    explored = [ [False] * num_cols for _ in range(num_rows)]
    largest_area = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if m[r][c]==1 and not explored[r][c]:
                neighbors=[(r,c)]
                area = 0
                while len(neighbors)!=0:
                    row,col=neighbors.pop()
                    if explored[row][col] != True:
                        explored[row][col]=True
                        area +=1
                        ##up
                        if row-1>=0 and m[row-1][col]==1 and not explored[row-1][col]:
                            neighbors.append((row-1,col))
                            
                        ##down
                        if row+1<num_rows and m[row+1][col]==1 and not explored[row+1][col]:
                            neighbors.append((row+1, col))
                            
                        ##right
                        if col+1<num_cols and m[row][col+1]==1 and not explored[row][col+1]:
                            neighbors.append((row, col+1))
                            
                        ##left
                        if col-1>=0 and m[row][col-1]==1 and not explored[row][col-1]:
                            neighbors.append((row,col-1))
                            
                if area > largest_area:
                    largest_area = area
    print(largest_area)
largestArea(binaryMatrix)
