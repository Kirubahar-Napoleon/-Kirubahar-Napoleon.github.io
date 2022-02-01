# LAMBDA EXPRESSION

# One of Pythons most useful (and for beginners, confusing) tools is the lambda expression. 
# lambda expressions allow us to create "anonymous" functions. 
# This basically means we can quickly make ad-hoc functions without needing to properly define a function using def.

# Function objects returned by running lambda expressions work exactly the same as those created and assigned by defs. 
# There is key difference that makes lambda useful in specialized roles:

#######lambda's body is a single expression, not a block of statements.
# The lambda's body is similar to what we would put in a def body's return statement. 
# We simply type the result as an expression instead of explicitly returning it. 
# Because it is limited to an expression, a lambda is less general that a def. We can only squeeze design, to limit program nesting. 
# lambda is designed for coding simple functions, and def handles the larger tasks.

# Lets slowly break down a lambda expression by deconstructing a function:

def square1(num):
    result = num**2
    return result

print(square1(4))




#We could simplify it as below:
def square2(num):
    return num**2

print(square2(6))



#We could actually even write this all on one line.
def square3(num): return num**2
print(square3(7))



#This is the form a function that a lambda expression intends to replicate. A lambda expression can then be written as:
square = lambda num: num **2
print(square(8))



#We could use this with Map and Filter as below
my_nums = [0,1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda num: num ** 2, my_nums)))
print(list(filter(lambda n: n % 2 == 0,my_nums)))



#Here are a few more examples
#** Lambda expression for grabbing the first character of a string: **
char = lambda s: s[0]
print(char('Viji'))



#** Lambda expression for reversing a string: **
rev = lambda s: s[::-1]
print(rev('Viji'))


#Sum of two nums
total = lambda x,y : x + y
print(total(10,30))

