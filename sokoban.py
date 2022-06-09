from random import randint
import msvcrt
import os, sys, time
from enum import Enum
from colorama import Fore, Back, Style, init 

player_row = 0
player_col = 0
TOTAL_GOALS = 3
BOARD_POS_ROW = 5
BOARD_POS_COL = 20 
BOARD_WIDTH = 16
BOARD_HEIGHT = 8 
BLANK_IMG = ' '
BLOCK_IMG = '▓'
GOAL_IMG = 'X'
PLAYER_IMG = 'Ö'
WALL_IMG = '▒'
game_board = [0 * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

def get_obj(x, y):
    if game_board[x][y] == 2:
        return "goal"
    if game_board[x][y] == 3:
        return "block"
    if game_board[x][y] == 0:
        return "space"

def randomly_place_object(obj):
    d = {0:"blank", 1:"", 2, 3}
    if obj == "goal":
        c = randint(0, BOARD_WIDTH-1)
        r = randint(0, BOARD_HEIGHT-1)
        while game_board[r][c] != 0:
            c = randint(0, BOARD_WIDTH-1)
            r = randint(0, BOARD_HEIGHT-1)
        game_board[r][c] = 2

    elif obj == "player":
        c = randint(0, BOARD_WIDTH-1)
        r = randint(0, BOARD_HEIGHT-1)
        while game_board[r][c] != 0:
            c = randint(0, BOARD_WIDTH-1)
            r = randint(0, BOARD_HEIGHT-1)
        game_board[r][c] = 1

    elif obj == "block":
        c = randint(0, BOARD_WIDTH-1)
        r = randint(0, BOARD_HEIGHT-1)
        while game_board[r][c] != 0:
            c = randint(0, BOARD_WIDTH-1)
            r = randint(0, BOARD_HEIGHT-1)
        game_board[r][c] = 3
        player_row = r
        player_col = c



def print_wall():
    row = 10
    col = 15
    print(Fore.RED + f'\033[{row};{col}H' + WALL_IMG * BOARD_WIDTH)
    for x in range(BOARD_HEIGHT):
        print(Fore.RED + f'\033[{row + x};{col}H' + WALL_IMG)
        print(Fore.RED + f'\033[{row + x};{col + BOARD_WIDTH - 1}H' + WALL_IMG)
    print(Fore.RED + f'\033[{row + BOARD_HEIGHT};{col}H' + WALL_IMG * BOARD_WIDTH)
    pass

def print_board(board):
    row = 10
    col = 15
    print_wall()
    for r in range(len(game_board)):
        for y in range(len(game_board[0])):
            if game_board[r][y] == 1:
                print(Fore.RED + f'\033[{row + r};{col + y}H' + PLAYER_IMG)
            if game_board[r][y] == 3:
                print(Fore.RED + f'\033[{row + r};{col + y}H' + BLOCK_IMG)
            if game_board[r][y] == 2:
                print(Fore.RED + f'\033[{row + r};{col + y}H' + BLANK_IMG)
    pass

def move_object(board, row, col, direction, obj):
    ''' 
    checks if object can be moved from current pos (row, col) to
    the direction specified.  If the move is possible, the object is
    moved and returns True, otherwise return False and the object is 
    not moved
    '''
    if direction == 1:
        if get_obj(row - 1, col) == "space":
            game_board[row][col] = 0
            game_board[row - 1][col] = obj
    if direction == 2:
        if get_obj(row + 1, col) == "space":
            game_board[row][col] = 0
            game_board[row + 1][col] = obj
    if direction == 1:
        if get_obj(row, col - 1) == "space":
            game_board[row][col] = 0
            game_board[row][col - 1] = obj
    if direction == 1:
        if get_obj(row, col + 1) == "space":
            game_board[row][col] = 0
            game_board[row][col + 1] = obj


# for windows OS 
os.system("cls")

import msvcrt
import ctypes

class _CursorInfo(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int),
                ("visible", ctypes.c_byte)]
ci = _CursorInfo()
handle = ctypes.windll.kernel32.GetStdHandle(-11)
ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
ci.visible = False
ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))

print_board(game_board)
randomly_place_object("player")
for x in range(TOTAL_GOALS):
    randomly_place_object("goal")
    randomly_place_object("block")
while True:
    if msvcrt.kbhit():
          c=msvcrt.getch()
          if c==b" ":
              print(Fore.GREEN+"\033[{};{}H".format(1, 20)+"space")
              if len(bullet_row_col) < 3:
                  bullet_row_col.append([car_row - 1, car_col+4])

          if c==b'\xe0':
            c=msvcrt.getch()

            if c==b"H":
              print(Fore.GREEN+"\033[{};{}H".format(1, 20)+"up")
              direction = 1

            elif c==b"P":
              print(Fore.GREEN+"\033[{};{}H".format(1, 20)+"down")
              direction = 2

            elif c==b"K":
              print(Fore.GREEN+"\033[{};{}H".format(1, 20)+"left")
              direction = 3

            elif c==b"M":
              print(Fore.GREEN+"\033[{};{}H".format(1, 20)+"right")
              direction = 4


    move_object(game_board, player_row, player_col, direction, 1)
    print_board(game_board)
    print(Fore.GREEN+"\033[{};{}H".format(1, 20)+str(game_board))
    print(Fore.GREEN+"\033[{};{}H".format(1, 20)+"left")

