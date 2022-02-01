# map function
# The map function allows you to "map" a function to an iterable object. 
# That is to say you can quickly call the same function to every item in an iterable, such as a list. For example:

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

print(list(map(square,my_nums)))


#The functions can also be more complex
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]

mynames = ['John','Cindy','Sarah','Kelly','Mike']
print(list(map(splicer,mynames)))


