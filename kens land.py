def find_land(land_map):
    list1 = []
    for x in range(len(land_map)):
        for y in range(len(land_map[0])):
            if land_map[x][y]:
                list1.append((x, y))
    return list1


print(find_land([[0,1,0,0,0,0],
                   		[1,1,0,0,0,0],
						[0,1,1,1,0,0],
						[0,1,0,1,0,0],
						[0,0,0,1,0,0]]))
