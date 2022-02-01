#Python Applies LEGB rule to assess the value for a variable.
# The precendence for a variable value is given to the local declaration if there is also one available globally. 
#If there is no Local Variable assigment available inside the function precendence is given to the function that encloses it
# If a local and enclosing local is not available, the Global Variable will be used and then the built in 

#Example

name = 'Shastika'

def greet():
    ##name = 'Viji'
    
    def hello():
        ##name = 'Kirubahar'
        print('Hello '+name)
    
    hello()

greet()


# #The global statement

# What if we want to process and also affect the value of a Global variable inside a function, then We have to tell Python that the name is not local, but it is global. 
# We do this using the global statement. 
# It is impossible to assign a value to a variable defined outside a function without the global statement.

# However, this is not encouraged and should be avoided since it becomes unclear to the reader of the program as to where that variable’s definition is. 
# Using the global statement makes it amply clear that the variable is defined in an outermost block.

x = 50

def func():
    global x   #This is the decalration inside function that we are going to affect the variable Globally
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)