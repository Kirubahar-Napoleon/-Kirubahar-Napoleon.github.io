# Apart form the arguments passed during class or method call, we can also define a Object attribute locally inside the class 
# This attribute will span across all the methods inside the class and can be used throughout the class as below.

# We could also call this object attribute outside the class via the class object as seen below as "k.name",

class Coa():

    name = 'Viji'

    def __init__(self,age):
        self.age = age
        print(f'name is {self.name} and age is {self.age}')
        print('the name can also be called as Class.Attribute format as "Coa.name" as seen here ()'.format(Coa.name))

    def say_hello(self):
        self.newname = Coa.name + ' Kirubahar'
        self.anothername = self.name + ' Kannan'
        print('Hello {} your age is {}'.format(self.newname, self.age))
        print('Hello {} your age is {}'.format(self.anothername, self.age))

k = Coa(29)
print(k.name)
print(k.age)
k.say_hello()
print(k.newname)
print(k.anothername)


# As you could see here, the class object attribute "name" defined right after the class declaration inside the class 
# This attribute can be called as class.attribute name or self.Attribute name inside the class.
	
# Also outside the class, the attribute can be called using object.attribute name as k.name here which returned "Viji" as value


# NOTE : 
# If you notice attribute call print(k.newname) and print(k.anothername) Has provided a valid output
#This will only work after the method say_hello() was called as k.say_hello(). 
# If these are called without calling the method first it will result in an error as below,

L = Coa(29)
print(L.name)
print(L.age)
print(L.say_hello())
print(L.anothername)
L.say_hello()
