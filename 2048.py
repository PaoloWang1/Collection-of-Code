import random
from transpose import matrix_transpose
from getkey import getch

gb = [[0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]]

placeholder = []
divider = ["|", "|", "|", ""]
line=  ["-", "-", "-", ""]
num_choices = [4]+[2]*9
cell_width = 5
def print_gm(m):
    for r in range(4):
        for c in range(4):
            print(str(m[r][c]).center(cell_width) if m[r][c] else " "*cell_width, end = divider[c])
        print("\n" + line[r]*23)
def spawn_block(m):
    r = random.randint(0,3)
    c = random.randint(0,3)
    while m[r][c] != 0:
        r = random.randint(0,3)
        c = random.randint(0,3)
    num = random.randint(0,9)
    if num == 0:
        m[r][c] = 4
    else:
        m[r][c] = 2
                
def shift_cells(cell_list):
    for y in range(cell_list.count(0)):
         cell_list.remove(0)
    x =0
    while x < len(cell_list)-1:
         if cell_list[x] == cell_list[x+1]:
              cell_list[x] = cell_list[x] + cell_list[x+1]
              cell_list.pop(x+1)
         x+=1
    for num in range(4-len(cell_list)):
         cell_list.append(0)
    return cell_list

def game_over(gb):
   for x in range(len(gb)):
       for y in range(len(gb)):
           if gb[x][y] == 0:
               return False
   for row in range(len(gb)):
       for col in range(1, len(gb[row])):
           if gb[row][col] == gb[row][col-1]:
               return False
   for col in range(1, len(gb)):
       for row in range(len(gb[col])):
           if gb[row][col] == gb[row][col-1]:
               return False
   return True

   
def play(m, direction):
    if direction == "down":
        m = matrix_transpose(m)
    if direction == "up":
        m = matrix_transpose(m)
        for x in range(len(m)):
            m[x].reverse()
    if direction == "right":
        for x in range(len(m)):
            m[x].reverse()
    for i in range(4):
        for y in range(m[i].count(0)):
            m[i].remove(0)
    print(m, direction)
    for y in range(len(m)):
        shift_cells(m[y])
    if direction == "up":
        m = matrix_transpose(m)
    if direction == "down":
        for x in range(len(m)):
            m[x].reverse()
        m = matrix_transpose(m)
        
    if direction == "right":
        for x in range(len(m)):
            m[x].reverse()
    return m





def play_game(gb):
    spawn_block(gb)
    while not game_over(gb):
        spawn_block(gb)
        print_gm(gb)
        while True:
            c = getch()
            if c[0] != 224:
                if c[0] == 72:
                    gb = play(gb, "up")
                    break
                if c[0] == 80:
                    gb = play(gb, "down")
                    break
                if c[0] == 77:
                    gb = play(gb, "right")
                    break
                if c[0] == 75:
                    gb = play(gb, "left")
                    break
                else:
                    print("The key you entered was not one of the arrow keys!")
    print("Game Over!")

play_game(gb)
        


    
gb=[[0,2,4,8],
    [2,4,8,2],
    [4,8,2,4],
    [8,2,4,2]]
print("Should be false: ", game_over(gb))

gb=[[4,2,4,8],
    [2,0,8,2],
    [4,8,2,4],
    [8,2,4,2]]
print("Should be false: ", game_over(gb))

gb=[[4,2,4,8],
    [2,4,8,2],
    [4,8,0,4],
    [8,2,4,2]]
print("Should be false: ", game_over(gb))

gb=[[4,2,4,8],
    [2,4,8,2],
    [4,8,2,4],
    [8,2,4,0]]
print("Should be false: ", game_over(gb))

gb=[[0,2,4,8],
    [2,4,8,2],
    [4,8,2,4],
    [8,2,4,0]]
print("Should be false: ", game_over(gb))

gb=[[0,2,4,8],
    [2,4,0,2],
    [4,8,2,4],
    [8,2,4,0]]
print("Should be false: ", game_over(gb))

gb=[[0,2,4,8],
    [2,4,0,2],
    [4,0,2,4],
    [8,2,4,0]]
print("Should be false: ", game_over(gb))


gb=[[4,2,4,8],
    [2,4,8,2],
    [4,8,2,4],
    [8,2,4,2]]
print("Should be true: ", game_over(gb))

gb=[[8,2,4,8],
    [2,4,16,2],
    [4,32,2,4],
    [8,2,4,64]]
print("Should be true: ", game_over(gb))

gb=[[4,2,2,8],
    [2,4,8,2],
    [4,8,2,4],
    [8,2,4,2]]
print("Should be false: ", game_over(gb))

gb=[[4,2,8,8],
    [2,4,8,2],
    [4,8,2,4],
    [8,2,4,2]]
print("Should be false: ", game_over(gb))

    
# test cases for shift_cells
# make sure your code can pass these test cases

sl=[0]*4
print(shift_cells(sl))

sl=[2,0,0,0]
print(shift_cells(sl))

sl=[0,2,0,0]
print(shift_cells(sl))

sl=[0,0,0,2]
print(shift_cells(sl))

sl=[0,2,0,4]
print(shift_cells(sl))

sl=[0,2,4,8]
print(shift_cells(sl))

sl=[2,2,0,0]
print(shift_cells(sl))

sl=[2,0,2,0]
print(shift_cells(sl))

sl=[2,0,0,2]
print(shift_cells(sl))

sl=[2,2,0,2]
print(shift_cells(sl))

sl=[2,0,2,2]
print(shift_cells(sl))

sl=[2,2,2,2]
print(shift_cells(sl))

sl=[4,2,4,2]
print(shift_cells(sl))

sl=[0,2,2,0]
print(shift_cells(sl))

sl=[0,2,2,4]
print(shift_cells(sl))

sl=[8,4,2,2]
print(shift_cells(sl))

sl=[2,2,8,4]
print(shift_cells(sl))

sl=[8,4,0,4]
print(shift_cells(sl))

sl=[2,16,4,4]
print(shift_cells(sl))

sl=[4,16,4,4]
print(shift_cells(sl))

sl=[2,2,16,8]
print(shift_cells(sl))

sl=[2,4,16,16]
print(shift_cells(sl))

sl=[2,2,0,32]
print(shift_cells(sl))

sl=[2,2,4,32]
print(shift_cells(sl))

sl=[0,8,8,2]
print(shift_cells(sl))

sl=[2,8,8,0]
print(shift_cells(sl))

sl=[2,0,8,8]
print(shift_cells(sl))
