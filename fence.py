def fence_units(map):
    fences_needed = 0
    d = 0
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y]:
                #print("This cell is 1: ", x, y)
                if x != len(map) - 1:
                    if not map[x + 1][y]:
                        d += 1
                else:
                    d += 1
                if x != 0:
                    if not map[x - 1][y]:
                        d += 1
                else:
                    d += 1
                if y != len(map[0]) - 1:
                    if not map[x][y + 1]:
                        d += 1
                else:
                    d += 1
                if y != 0:
                    if not map[x][y - 1]:
                        d += 1
                else:
                    d += 1
                #print("This cell has this much fence ", d)

    return d

print(fence_units([[0,1,0,0,0,0],[1,1,0,0,0,0],[0,1,1,1,0,0],[0,1,0,1,0,0],[0,0,0,1,0,0]]))
