xo = ["   ", " X ", " O "]
gb = [[0,0,0],
      [0,0,0],
      [0,0,0]]
divider = ["|", "|", ""]
line=  ["-"*11, "-"*11, ""]
def print_gm(m):
    print()
    for m in range(3):
        for col in range(3):
            print(xo[gb[m][col]], end = divider[col])
        print()
        print(line[m])
    count1 = 1
    for row in range(3):
        for col in range(3):
            print(str(row*3+col+1).center(3) if not gb[row][col] else '   ', end = divider[col])
        print()
        if count1 < 3:
            print("-"*11)
            count1 +=1
    print()

print_gm(gb)

win = 0


def check_game(m):
   winner = ''
   coun = 0
   for row in range(len(m)):
       if m[row][0] and len(set(m[row]))==1:
           winner = xo[m[row][0]]
   for col in range(len(m[0])):
       if m[0][col] and len(set([m[r][col] for r in range(len(m))]))==1:
           winner = xo[m[0][col
                            ]]
   if  m[0][0] and m[0][0] == m[1][1] == m[2][2]:
       winner = xo[m[0][0]]
   if m[0][2] and m[0][2] == m[1][1] == m[2][0]:
       winner = xo[m[1][1]]
   if winner == '':
       for x in range(len(m)):
           for y in range(len(m[0])):
               if m[x][y] == 0:
                   return False, 0
       winner = 'tie'
   return True, winner
moves = 0
player = 1
    
def AI(gb):
    total_moves = 9 - sum([row.count(0) for row in gb])
    if total_moves == 1:
        if gb[1][1]==1:
            return (0,0)
        else:
            return (1,1)
    
#Check if you need to take a win
    for x in range(3):
        for y in range(3):
            if gb[x][y]==0:
                gb[x][y]=2
                if check_game(gb)[0]:
                    gb[x][y]=0
                    return(x,y)
                gb[x][y]=0
    
#check if you need to block
    for x in range(3):
        for y in range(3):
            if gb[x][y]==0:
                gb[x][y]=1
                if check_game(gb)[0]:
                    gb[x][y]=0
                    return(x,y)
                gb[x][y] = 0
        
#special cases count

    sides = [gb[0][1], gb[1][0], gb[2][1], gb[1][2]].count(1)
    corners = [gb[0][0], gb[0][2], gb[2][0], gb[2][2]].count(1)
    middle = 1 if gb[1][1]==1 else 0
    
#case 1
    if middle == 1 and corners == 1 and total_moves < 4:
        return(0,2)
    
#case 2
    elif sides == 1 and corners == 1 and total_moves < 4:
        return(2,2) if gb[1][2]==1 or gb[2][1]==1 else(0,0)
    
#case 3
    elif sides == 2 and total_moves < 4:
        return(2,0) if gb[2][1]==1 else(0,2)

#case 4
    elif corners == 2 and total_moves < 4:
        return(0,1)
        

#take any empty stop
    else:
        for r in range(3):
            for c in range(3):
                if gb[r][c]==0:
                    return(r,c)

while not check_game(gb)[0]:
    choice = int(input("Player 1, what is your choice?"))
    if choice < 4:
        gb[0][choice-1] = 1
    elif choice < 7:
        gb[1][choice-4] = 1
    else:
        gb[2][choice - 7] = 1
    print_gm(gb)
    moves+=1
    if moves != 9:
        gb[AI(gb)[0]][AI(gb)[1]] = 2
        print_gm(gb)
    moves += 1

if moves == 10:
    print("It's a tie!")
else:
    print(check_game(gb)[1] + " wins!")




        
