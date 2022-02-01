mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']

myziplist = list(zip(mylist1,mylist2))
print(myziplist)


#We could also use zip operator in a for loop as below

for item1, item2 in zip(mylist1,mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))


#Zip can also span across more than two list as below
mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']
mylist3 = [100,200,300,400,500]
myziplist = list(zip(mylist1,mylist2,mylist3))
print(myziplist)

#What if the list are not of same size ? zip will still work on it but will restrain it to the lowest size of the list available as below

mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']
mylist3 = [100,200,500]
myziplist = list(zip(mylist1,mylist2,mylist3))
print(myziplist)