# filter function

# The filter function returns an iterator yielding those items of iterable for which function(item) is true. 
# Meaning you need to filter by a function that returns either True or False. 
# Then passing that into filter (along with your iterable) and you will get back only the results that would return True when passed to the function.


#Example

def check_even(num):
    return num % 2 == 0 

nums = [0,1,2,3,4,5,6,7,8,9,10]

print(list(filter(check_even,nums)))