#Sets are represented within {} but are not dicstionarry which are referenced using a key value pair, instead thye are unordered collection of unique elements
# example 

#Creating a sample set here
from typing import ItemsView


myset = set()

# adding values to the sets now
myset.add(4)
myset.add(2)
myset.add(1)

# Printing the set value now
print(myset)

# now lets add more to it
myset.add(4)
myset.add(5)
myset.add(1)
myset.add(2)
myset.add(3)

#Now printing the set again
print(myset)
print('as you can see Set does not take duplicate values')

#we can cast a list to set as below also a set can have any type of value in it
mylist= [1,2,3,4,5,6,7,8,9,8,7,6,'a','b','c','d',5,4,3,2,1,1,'a',1.5,2.8,2.3,1.5]
myset=set(mylist)
print('mylist is now {}'.format(mylist))
print(f'my set of the mylist is {myset}')