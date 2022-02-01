from random import shuffle
from random import randint

mylist = [10,20,30,40,100]


# The shuffle operates "in-place" meaning it won't return anything, instead it will effect the list passed
shuffle(mylist)
print(mylist)


# Return random integer in range [a, b], including both end points.
print(randint(0,100))
print(randint(0,100))
print(randint(0,100))
