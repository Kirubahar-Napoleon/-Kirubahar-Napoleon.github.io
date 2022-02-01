
x = 0

while x < 10:
    print('x is currently: {} which is less 10 so we are adding one to x'.format(x))
    x+=1



#While loop with else

y = 0

while y < 10:
    print('y is currently: {} which is less 10 so we are adding one to y'.format(y))
    y+=1
else:
    print('All Done!')


#While loop works with BREAK, CONTINUE and PASS

#Here let us print continuing.... for all iteration, but we want it to be not printed when x is equal to 3
x = 0

while x < 10:
    print('x is currently: {} which is less 10 so we are adding one to x'.format(x))
    x+=1
    if x==3:
        print('x is now 3 so we will not print the contnuig.... word for it now')
        continue
    else:
        print('continuing...')
        

#Here we are doing a similar operation but stopping the iteration, once x value reaches 3
x = 0
while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('Breaking because x==3')
        break
    else:
        print('continuing...')
        
