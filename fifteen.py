# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 11:35:05 2017

@author: warrenl0134
"""

n = int(input("please enter a value: "))
board = []

def make_board(n):
    """
n is an integer between 3 and 9.  makes a board which is a list of n lists, each list 
representing a row in the board.  assigns a value from the (n*n - 1) to 0 to each tile.  
prints out the board as a two dimensional array of values. if n is even, the 2 and 1 tiles are swapped.
    """
    global board
    max = n * n #the number of tiles in the board
    count = 1 #a counter to change the value assigned to each tile
    for i in range(n):
        board.append([]) #appends a list inside the list of board.  Essentially creates a row which is of type list.
        for j in range(n): 
            num = max - count 
            if num == 0: #the 0 tile will display like a blank space
                tile = '  '
            elif num < 10: #adds a space to tile values less than 10 for formatting.
                tile = ' ' + str(num)
            else:
                tile = str(num) 
            board[i].append(tile) #appends a tile value to each row, n number of times.
            count += 1
    if n % 2 == 0:
        board[-1][-3] = ' 1'
        board[-1][-2] = ' 2'
    for row in board:
        print(' '.join(row)) #prints the values in the row as a string separated by ' '.
 
def find_blank(board):
    """
    Takes the board as input and returns a tuple which contains the row and column 
    location of the blank tile.
    """
    for i in range(n):
        for j in range(n):
            if board[i][j] == '  ':
                return(i, j)

def find_tile(tile):
    """
    Tile is a string value that the user inputs.  
    The function returns a tuple which is the row and column values of the location 
    of the tile on the board.
    """
    for i in range(n):
        for j in range(n):
            if board[i][j] == tile or board[i][j] == ' '+tile:
                return(i, j)

def next_to_blank(blank, tile_to_move):
    """
    Blank is a tuple of the row and column location of the blank tile.  
    Tile is a tuple containing the row and column location of the tile to be moved. 
    Only tiles adjacent to the blank tile can be moved.
    The function returns True if the tile is adjacent to the blank tile and False if it is not.
    """
    
    return abs(tile_to_move[0] - blank[0]) + abs(tile_to_move[1] - blank[1]) == 1 #manhattan distance
        
def update_tiles(blank, tile_to_move):
    """
    Blank is a tuple of the row and column location of the blank tile. 
    Tile is a tuple containing the row and column location of the tile to be moved. 
    Swaps the position of the blank tile and tile to be moved.  Prints the updated board after swap.
    """
    
    if next_to_blank(blank, tile_to_move):
        (board[blank[0]][blank[1]], board[tile_to_move[0]][tile_to_move[1]]) = \
        (board[tile_to_move[0]][tile_to_move[1]], board[blank[0]][blank[1]])
    for row in board:
        print(' '.join(row)) 
        
def check_for_win(board):
    """
    Takes the board as input and checks to see if all the tiles are in order from least to greatest.  
    Returns False if they are not and True if board is complete.
    """
    if board[-1][-1] != "  ":
        return False
    x = 1
    for row in board:
        for i in row:
          if i == "  ":
              continue
          if int(i) != x:
              return False
          else:
              x = x + 1
    return  True

make_board(n)
while check_for_win(board) == False:
    blank = find_blank(board)
    tile= input("please enter a tile: ")
    tile_to_move = find_tile(tile)
    update_tiles(blank, tile_to_move)
print("you won! :)")

#TODO - implement the playing of the game. 
# Use the functions above and a couple of more lines to complete the playing of the game. 
   
 


