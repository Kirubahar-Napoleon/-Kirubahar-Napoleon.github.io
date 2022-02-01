for i in ['a',2,'b','c',5]:
    try:
        print(i**2)
    except TypeError:
        print('Unsupported Input')


x = 5
y = 0

try : 
    z = x/y
except ZeroDivisionError:
    print('Division by Zero will yeild Infinte value, please check your input')

#Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

Square = lambda a : a**2

while True:
    try:
        num = int(input('Please enter a number:'))
        print(Square(num))
    except :
        print('The input provided is not a valid Integer')
        continue
    else :
        print('Thanks for using our service')
        break