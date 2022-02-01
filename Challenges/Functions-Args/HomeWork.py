#CHALLENGE 1
#Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
#Example
#lesser_of_two_evens(2,4) --> 2
#lesser_of_two_evens(2,5) --> 5

def less(a,b):
    if a % 2 == 0  and b % 2 == 0:
        return min(a,b)
    else:
        return max(a,b)
print(less(4,6))


#CHALLENGE 2
# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal(word):
    wordl = word.lower().split()
    return wordl[0][0] == wordl[1][0]

print(animal('Levelheaded llama'))


#CHALLENGE 3
# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

def twenty(a,b):
    return (a+b)==20 or a==20 or b==20

print(twenty(10,10))


#CHALLENGE 4
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald'

def cap(word):
    return (word[0:3].capitalize() + word[3:].capitalize())

print(cap('Vijaya'))

#CHALLENGE 5
# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
# Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:

def yoda(word):
    return ' '.join(word.split()[::-1])

print(yoda('Here we are'))


#CHALLENGE 6
# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
# Note: abs(num) returns the absolute value of a number

def find100(n):
    return abs(n-100) <= 10 or abs(n-200) <= 10

print(find100(209))


#CHALLENGE 7
# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def find33(ls):
    for i in range(0,(len(ls)-1)):
        if ls[i] == 3 and ls[i+1] == 3:
            return True
    return False

print(find33([1,3,4,5,3]))
print(find33([1,3,3,5,6]))


#CHALLENGE 8
# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def doll(word):
    dollword = ''
    for char in word:
        dollword += char*3
    return dollword

print(doll('Viji'))


#CHALLENGE 9
# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

def jack(a,b,c):
    total = sum((a,b,c))
    if total <= 21:
        return total
    elif (a==11 or b==11 or c==11) and total <= 31:    #Another way to check this is "elif total <=31 and 11 in (a,b,c):"
        return total-10
    else:
        return 'Bust'

print(jack(11,11,10))


#CHALLENGE 10
# SUMMER OF '69: Return the sum of the numbers in the array, 
# except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). 
# Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

def summer(nums):
    add = True
    total = 0
    for i in nums:
        while add:
            if i != 6:
                total += i
                break
            else:
                add = False
        while not add:
            if i != 9:
                break
            else:
                add = True
                break
    return total

print(summer([1, 3, 5]))
print(summer([1, 3, 5, 6, 9, 10]))
print(summer([2, 1, 6, 9, 11]))



#CHALLENGE 11
# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False

def spy(nums):
    #To solve such issues, we could create a reference list to match original list. 
    # To prevent all numbers being matche in this refernce list, we could add a alphabet to the list which will not be matched with the incoming list
    mylist = ['x',7,0,0]
    for num in nums:
            if num == mylist[-1]:
                mylist.pop()
    return len(mylist) == 1

print(spy([1,2,4,0,0,7,5]))



#Not done by me
#CHALLENGE 12
# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25
#By convention, 0 and 1 are not prime.

def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes(100))

#Alternatively we could do this as below,

def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes2(100))



#Not done by me
#CHALLENGE 13
# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
# print_big('a')
# out:   *  
#       * *
#      *****
#      *   *
#      *   *
# HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
# For purposes of this exercise, it's ok if your dictionary stops at "E".

def big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

print(big('d'))