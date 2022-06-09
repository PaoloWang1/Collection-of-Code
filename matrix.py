list = [[0,1,2,3],[4,5,6,7],[8,9,10,11]]
length = len(list[0])
new_list = [[],[],[],[]]
for x in range(0, len(list)):
    for i in range(0, length):
        new_list[x].append(list[x][i])
print(new_list)
        
