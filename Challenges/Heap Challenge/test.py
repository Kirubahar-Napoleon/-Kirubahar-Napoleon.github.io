import os
from tabulate import tabulate

validin = True
ttt1 = ["","",""]
ttt2 = ["","",""]
ttt3 = ["","",""]
board = [ ttt1, ttt2, ttt3]
i = 1
check = True

def display_board(ttt):
    clear = lambda: os.system('clear')
    clear()
    print(tabulate(ttt,tablefmt='grid'))

while True:
    print('Player 1 Please choose whether you would like to play with X or O : ')
    player1 = input('')
    if player1.upper() in ('X','O'):
        print("Game Starts now")
        display_board(board)
        if player1.upper() == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
        break

def playerinput(val):
    global i
    while True:
        choice = input('Please choose a valid number between 1 and 9 :')
        if choice.isdigit() and int(choice) in range(1,10):
            break
    choice = int(choice)
    if choice <= 3 and ttt3[choice-1] == "":
        ttt3[choice-1] = val
        i += 1
    elif choice > 3 and choice <= 6 and ttt2[choice-4] == "":
        ttt2[choice-4] = val
        i += 1
    elif ttt1[choice-7] == "":
        ttt1[choice-7] = val
        i += 1
    else:
        print('The chosen position is already filled, Please choose another number')
        playerinput(val)
    

for x in range(0,9):
    if i % 2 != 0 : 
        playerinput(player1)
    else:
        playerinput(player2)
    display_board(board)