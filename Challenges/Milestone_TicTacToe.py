import os
from tabulate import tabulate

win = False
gameon = True

ttt1 = ["7","8","9"]
ttt2 = ["4","5","6"]
ttt3 = ["1","2","3"]
board = [ ttt1, ttt2, ttt3]
i = 1
count = 1

def display_board(ttt):
    clear = lambda: os.system('clear')
    clear()
    print(tabulate(ttt,tablefmt='grid'))

while True:
    print('Player 1 Please choose whether you would like to play with X or O : ')
    player1 = input('')
    player1 = player1.upper()
    if player1 in ('X','O'):
        print("Game Starts now")
        display_board(board)
        if player1 == 'X':
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
    if choice <= 3 and ttt3[choice-1] not in ('X','O'):
        ttt3[choice-1] = val
        i += 1
    elif choice > 3 and choice <= 6 and ttt2[choice-4] not in ('X','O'):
        ttt2[choice-4] = val
        i += 1
    elif choice > 6 and ttt1[choice-7] not in ('X','O'):
        ttt1[choice-7] = val
        i += 1
    else:
        print('The chosen position is already filled, Please choose another number')
        playerinput(val)
    

def wincheck():
    if (ttt1[0] == ttt1[1] == ttt1[2]) or (ttt2[0] == ttt2[1] == ttt2[2]) or (ttt3[0] == ttt3[1] == ttt3[2]):
        return True
    elif (ttt1[0] == ttt2[0] == ttt3[0]) or (ttt1[1] == ttt2[1] == ttt3[1]) or (ttt1[2] == ttt2[2] == ttt3[2]):
        return True
    elif (ttt1[0] == ttt2[1] == ttt3[2]) or (ttt1[2] == ttt2[1] == ttt3[0]):
        return True
    else:
        pass
    return False


while gameon:
    if count <= 9:
        count += 1 
    else:
        print('Game has been Drawn')
        break
    player = 1
    if i % 2 != 0 : 
        playerinput(player1)
    else:
        player = 2
        playerinput(player2)
    display_board(board)
    win = wincheck()
    if not win:
        gameon = True
    else:
        print(f'Congratulations Player{player} has won the game')
        gameon = False
        break