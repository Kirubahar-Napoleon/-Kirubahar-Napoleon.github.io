a = 'x' in ['x','y','z']
print(a)

b = 'x' in [1,2,3]
print(b)

c = 'x' not in ['x','y','z']
print(c)

d = 'x' not in [1,2,3]
print(d)

#We can use In and NotIn operators to check for a variable existence in a list or dictionary or tuples etc as below,

mylist = ['a','b','c','d','e','f','g','h']

if 'a' in mylist:
    print('letter a exist in the list')

if 'x' in mylist:
    print('letter x exist in the list')
else:
    print('letter x is not in the given list')


#Use of In in Dict
mydict = {'user1': 6,'user2': 9,'user3': 15}
if 'user1' in mydict.keys():
    print('this key exist')
else:
    print('this key does not exist')


if 10 in mydict.values():
    print('this value exist')
else:
    print('this value does not exist')


if ('user3',9) in mydict.items():
    print('the key value pair exists')
elif ('user3',15) in mydict.items():
    print('the key value pair "user3",15 exists')
else:
    print('Given Key Value Pair does not exist')

