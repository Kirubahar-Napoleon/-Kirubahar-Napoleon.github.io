#Write a function that computes the volume of a sphere given its radius.

vol = lambda rad : (rad**3)*(4/3)*3.14

print(vol(2))

#Write a function that checks whether a number is in a given range (inclusive of high and low)

check = lambda a,b,c : a in range(b,c+1)

print(check(5,2,7))
print(check(9,2,7))

#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output : 
# No. of Upper case characters : 4
# No. of Lower case Characters : 33

def casecheck(word):
    lower = 0
    upper = 0
    for char in word:
        if char.islower():
            lower += 1
        elif char.isupper():
            upper += 1
    print(f'No. of Lower case characters : {lower}')
    print(f'No. of Upper case characters : {upper}')

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
casecheck(s)

#Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

unique = lambda num: list(set(num))

print(unique([1,1,1,1,2,2,3,3,3,3,4,5]))



#Write a Python function to multiply all the numbers in a list.
# Sample List : [1, 2, 3, -4]
# Expected Output : -24

def mul(lst): 
    x = 1
    for num in lst: 
        x = x*num
    return x 
print(mul([1,2,3,4,5]))

# Write a Python function that checks whether a word or phrase is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run". 
# Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. 
# Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.

def pal(word): return word.replace(' ','').lower()[::-1] == word.replace(' ','').lower()

print(pal('Ma y am'))


# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

def pang(word):
    lst = []
    lst[:0] = word.replace(' ','').lower() #This will help to remove the space and convert the characters to lower case. Also this converts the string variable into a list - character wise
    return len(set(lst)) == 26

print(pang("The quick brown fox jumps over the lazy dog"))

#Alternatively
def pang1(word): return len(set(word.replace(' ','').lower())) == 26

print(pang1("The quick brown fox jumps over the lazy dog"))