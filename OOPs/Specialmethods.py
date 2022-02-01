#When we print a class object we would get an output of the memory location where the object is saved in our system as below

from crypt import methods
from operator import methodcaller


class Special():

    def __init__(self) -> None:
        print('Hello')


s = Special()
print('lets print the object now')
print(s)

#As we could see we got <__main__.Special object at 0x103e9b700> for "print(s)"

# What if we want python to print out something about the object or a standard output when object is printed ?
# thats when we could use the special methods
# some of the special methods are __str__, __len__, __del__ etc

#the __str__ method response is what is printed when print() command is used
#__len__ is responded when len() is used for the object
#Note : We dont use print command under str and len, instead we use return

#del is created to delete the object instance from the memory

print('\n')
print('\n')

class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages


    def __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)


    def __len__(self):
        return self.pages


    def __del__(self):
        print("Book Object destroyed")


B = Book(title ='Life of Napoleon',author = 'Kirubahar Napoleon', pages=50)
print(B)
print(len(B))
del B
print(B)

#As we could see here print B after the del has raised an error as name B not defined,  
#This is beciase the del method has deleted the object instance from the memory.
