import utilities
import random

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

print("Welcome to Tic Tac Toe! Player X will go first, followed by Player O. The grid is numbered as seen below.")

utilities.print_positions()

print("On your turn, enter the number of an open spot to place your mark. The first player to get three marks in a row is the winner!")

turn = 0
tie = True
start = False
play_computer = False

print('\nDo you want to play against the computer?\nEnter y or n.')
# Player chooses whether or not to play computer
while not start:
    response = input()
    if response == 'y':
        play_computer = True
        start = True
    elif response == 'n':
        start = True

# Randomly choose who goes first
turn = random.randint(0, 1)
player = 'X' if turn == 0 else 'O'
print(f'\n{player} goes first!')

while ' ' in board:
    if play_computer and turn % 2 != 0:
        space = str(random.randint(1,9))
    else:
        space = input()
    # repeat turn if user picks anything outside of 1-9
    if space not in utilities.valid_numbers():
        print('Pick a number 1 - 9')
        continue
    else:
        space = int(space)
    # repeat this step if user picks filled space
    if board[space - 1] != ' ':
        print('try again')
        continue
    
    if turn % 2 == 0:
        board[space - 1] = 'X'
    else:
        board[space - 1] = 'O'
    
    utilities.print_board(board)
    turn += 1
    # horizontal matches
    if board[0] == board[1] == board[2] != ' ':
        tie = False
        print('Player {} wins!'.format(board[space - 1]))
        break
    elif board[3] == board[4] == board[5] != ' ':
        tie = False
        print('Player {} wins!'.format(board[space - 1]))
        break
    elif board[6] == board[7] == board[8] != ' ':
        tie = False
        print('Player {} wins!'.format(board[space - 1]))
        break
    # vertical matches
    elif board[0] == board[3] == board[6] != ' ':
        tie = False
        print('Player {} wins!'.format(board[space - 1]))
        break
    elif board[1] == board[4] == board[7] != ' ':
        tie = False
        print('Player {} wins!'.format(board[space - 1]))
        break
    elif board[2] == board[5] == board[8] != ' ':
        tie = False
        print('Player {} wins!'.format(board[space - 1]))
        break
    # diagonal matches
    elif board[0] == board[4] == board[8] != ' ':
        tie = False
        print('Player {} wins!'.format(board[space - 1]))
        break
    elif board[2] == board[4] == board[6] != ' ':
        tie = False
        print('Player {} wins!'.format(board[space - 1]))
        break
    
    if ' ' not in board and tie == True:
        print('It\'s a tie!')
    

# Requirements to complete:
#
#  * Every turn, display a grid in the console containing 
#    either X, O, or a space (" ") in each of the 9 spots. 
#
#  * In the console, the current player (X or O) enters a 
#    number 1 - 9 in order to designate where they would like 
#    to place their move
# 
#  * When a match is made (3 in a row, 3 in a column, or 3 diagonally)
#    the program ends and declares a winner.
#
#  * If the board is full and there is no winner, the program 
#    declares a tie.
