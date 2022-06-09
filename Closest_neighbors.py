'''def closest_neighbors(num_rows, num_cols, house_row, house_col):
    d = {}
    f = []
    for row in range(num_rows):
        for col in range(num_cols):
            if row != house_row or col != house_col:
                distance = abs(row - house_row) + abs(house_col - col)
                d[(row, col)] = distance
                print(row, col)

    g = sorted(d.items(), key=lambda x:x[1])
    for x in g:
        f.append(x[0])
    return f

print(closest_neighbors(3, 4, 1, 2))
'''

# ring method

def closest_neighbors(num_rows, num_cols, house_row, house_col):
    f = []
    img_map = [[0 for x in range(num_cols)] for y in range(num_rows)]
    print(img_map)
    largest_distance = 0
    corners = [(num_cols, num_rows), (0, num_rows), (num_cols, 0), (0,0)]
    for x in corners:
        num = abs(house_col - x[0]) + abs(house_row - x[1])
        if num > largest_distance:
            largest_distance = num
    inbound = lambda x, y : 0 <= x < num_cols and 0 <= y < num_rows
    for ring in range(largest_distance + 1):
        x, y = house_col - ring, house_row
        print(x, y)
        for move in [(1, 1),(1, -1),(-1, -1),(-1, 1)]:
            for d in range(ring):
                if inbound(x, y):
                    f.append((x, y))
                x += move[0]
                y += move[1]

    return f

print(closest_neighbors(2,5,1,4))
