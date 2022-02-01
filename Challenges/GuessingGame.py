import random
randomint = random.randint(1,100)
Guess = []
print('This is a Guessing game where you have to guess a number that the computer has guessed it Already')
print('The Rule is that the number should be between 1 and 100 \nIf Your first Guess is within 10 of the number I will return WARM \nIf not I will retun cold and you could keep entering the number until we find it' )
print('On all subsequent turns, if a guess is closer to the number than the previous guess, We will return "WARMER!" and if it is Farther we will retunr "Colder!"\n\nLets Start')

while True:
    UserVal = int(input('Please enter a input value : '))
    Guess.append(UserVal)
    if UserVal > 100 or UserVal < 1:
        UserVal = input('Value entered is outside the said range, please enter a new number between 1 and 100 : ')
        Guess.pop()
    elif UserVal == randomint:
        print('You have Guessed it correctly on your {} try, Well Done'.format(len(Guess)))
        break
    elif len(Guess) == 1 :
        if abs(Guess[-1] - randomint) <= 10:
            print('Warm')
        else:
            print('Cold')
    else:
        if abs(Guess[-1] - randomint) <= abs(Guess[-2] - randomint):
            print('Warmer!')
        else:
            print('Colder!')