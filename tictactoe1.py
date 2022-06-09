#Tic-Tac-Toe using two dimensional array

# This procedure prints the game table showing the Xs, Os, and empty slots
# and the number to enter for the empty slots.
#
#
# Input:
#   gb: game board (contains the 2 dimensional list holding the game board
gb = [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]
xo_str=[' ','O','X']
# Return: Nothing
#
# Special characters: | -
def print_board(gb):
    for x in range(3):
        for y in range(3):
            print(' ' + xo_str[gb[x][y]] + ' ', end='')

            print('|', end='')

        print('')
        print('-'*11)

    
# This procedure checks if the game is over
# returns a Bool type and the player who won:
#   True/False indicating if the game is over
#   The winner (value of 1 or 2) or 0 for tie
#
# Input:
#   gb: game board (a two dimensional list)
#
# Return:
#   Bool, Winner: Winner can be represented by 'X', 'O' or 1, 2 depending on
#                   how you want to represent each player, and need another
#                   symbol for a tie
def check_game_over(gb):
    return True, 0      # Game over, we have a tie
    # return True, 1    # Game over, 'O' won
    # return True, 2    # Game over, 'X' won
    # return False, 0   # Game is not over


##################################
# Start of main code
##################################
game_board = [[0]*3 for _ in range(3)]  # 3x3 list to hold the game board
                                        # 0: empty slot
                                        # 1: O
                                        # 2: X
                                        # You can use other representations:
                                        # ' ': empty slot
                                        # 'O': O
                                        # 'X': X

#Test cases                                    
print([[0,0,0],[0,0,0],[0,0,0]])
print_board([[0,0,0],[0,0,0],[0,0,0]])
print("\n",[[0,1,0],[0,1,0],[0,1,0]])
print_board([[0,1,0],[0,1,0],[0,1,0]])
print("\n",[[1,0,1],[1,0,1],[1,0,1]])
print_board([[1,0,1],[1,0,1],[1,0,1]])
print("\n",[[0,2,0],[0,2,0],[0,2,0]])
print_board([[0,2,0],[0,2,0],[0,2,0]])
print("\n",[[2,0,2],[2,0,2],[2,0,2]])
print_board([[2,0,2],[2,0,2],[2,0,2]])
print("\n",[[2,1,2],[1,2,1],[2,1,2]])
print_board([[2,1,2],[1,2,1],[2,1,2]])
