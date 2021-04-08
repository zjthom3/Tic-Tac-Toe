def print_board(board_list): 
  print('''
   {} | {} | {}
  -----------
   {} | {} | {}
  -----------
   {} | {} | {}
   '''.format(*board_list))

def print_positions():
  print_board(range(1, 10))

def valid_numbers():
    numbers = []
    x = range(1, 10)
    for n in x:
        numbers.append(str(n)) 
    return numbers

def play_computer():
    play = input()
    if play == 'y':
        return True
    return False