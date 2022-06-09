def paint(matrix):
    area = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[1])):
            if matrix[x][y] != 0:
                if x > 0:
                    d = matrix[x][y] - matrix[x-1][y]
                    if d > 0:
                        area += d
                else:
                    area += matrix[x][y]
                if x < len(matrix) - 1:
                    d = matrix[x][y] - matrix[x+1][y]
                    if d > 0:
                        area += d
                else:
                    area += matrix[x][y]
                if y > 0:
                    d = matrix[x][y] - matrix[x][y - 1]
                    if d > 0:
                        area += d
                else:
                    area += matrix[x][y]
                if y < len(matrix[0]) - 1:
                    d = matrix[x][y] - matrix[x][y + 1]
                    if d > 0:
                        area += d
                else:
                    area += matrix[x][y]
                area += 1

            """
            if y == 0:
                area += matrix[x][y]
            else:
                area += abs(matrix[x][y] - matrix[x][y-1])
            area += 1
            if y == len(matrix[1]) - 1:
                area += matrix[x][y]
            if x == 0:
                area += matrix[x][y]
            else:
                area += abs(matrix[x][y] - matrix[x-1][y])
            if y == len(matrix) - 1:
                area += matrix[x][y]
"""
    return area
print(paint([[1,2],[3,4]]))
