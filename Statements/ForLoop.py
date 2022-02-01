

#Iterating through the list
list1 = [1,2,3,4,5,6,7,8,9,10]

for num in list1:
    print(num)



#Using If inside a for loop to perform conditional based iteration operation
for num in list1:
    if num % 2 == 0:
        print(num)

for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print('Odd number')



# Start sum at zero
list_sum = 0 

for num in list1:
    list_sum += num

print(list_sum)


#To work with strings
inum = 0
for letter in 'This is a string.':
    if letter == 'i':
        inum += 1

print('number of time letter "i" occured in the string is {}'.format(inum))


#To work with tuples
tup = (1,2,3,4,5)

for t in tup:
    print(t)


#To work with list that has tuples values

list2 = [(2,4),(6,8),(10,12)]
for tup in list2:
    print(tup)

for (t1,t2) in list2:
    print(t1)



#To work with Dictionary
d = {'k1':111,'k2':22,'k3':333}

for item in d:
    print(item)

#Now lets try to unpack the dicstionary like tuples and lists
#If you notice, this method has an issue where only the first index of the key and the value is used in the output and not the entire output

for key,value in d:
    print('The Key value Pair is {} and {}'.format(key,value))



#So how can we get the values? Or both the keys and the values then?
#We can use Dictionary methods like  .keys(), .values() and .items()
#In Python each of these methods return a dictionary view object. 
# It supports operations like membership test and iteration, but its contents are not independent of the original dictionary – it is only a view
#For Example

print(d.items())
print(d.keys())
print(d.values())

#To unpack dictionary we could use below code
for k,v in d.items():
    print(k)
    print(v)


#If we want to obtain a true list of keys, values, or key/value tuples, you can *cast* the view as a list:
print(list(d.keys()))
print(list(d.values()))


#Remember that dictionaries are unordered, and that keys and values come back in arbitrary order. You can obtain a sorted list using sorted():
print(sorted(d.values()))



