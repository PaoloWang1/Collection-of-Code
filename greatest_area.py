def greatest_area(map):
    to_explore = []
    explored = [[False] * len(map[0]) for x in range(len(map))]
    largest = 0
    for x in range(len(map)):
        for y in range(len(map[0])):
            if not explored[x][y] and map[x][y]:
                to_explore.append([x, y])
                current_area = 0
                while len(to_explore) > 0:
                    r, c = to_explore.pop()
                    if not explored[r][c]:
                        current_area += 1
                        explored[r][c] = True
                        if x != len(map) - 1:
                            if map[x + 1][y]:
                                to_explore.append([x + 1][y])
                        if x != 0:
                            if map[x - 1][y]:
                                to_explore.append([x - 1][y])
                        if y != len(map[0]) - 1:
                            if map[x][y + 1]:
                                to_explore.append(map[x][y + 1])
                        if y != 0:
                            if not map[x][y - 1]:
                                to_explore.append(map[x][y - 1])
                largest = max(largest, current_area)

    return largest

