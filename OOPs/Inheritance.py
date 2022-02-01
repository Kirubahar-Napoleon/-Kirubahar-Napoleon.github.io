# Inheritance is way of Python that allows us to define a base class and extend its attributes in child class
# This is Very useful when you want to define a few set of characteristics that are unique for multiple object types 



class Family():

    surname = 'Napoleon'

    def __init__(self) :
        self.surname = Family.surname

    def your_family(self):
        print('I belong to {} family'.format(self.surname))

    def family_mem(self):
        raise NotImplementedError("This method neeeds to be called with in the child class")

class Kirubahar(Family):

    def __init__(self,mem1,mem2,loc='Ireland'):
        self.mem1 = mem1
        self.mem2 = mem2
        self.loc = loc
    
    def family_mem(self):
        print('Kirubahar Family Created, the members are {} and {}'.format(self.mem1,self.mem2))

    def location(self):
        print(f'Kirubahar {self.surname} family lives in {self.loc}')


class Karthik(Family):

    def __init__(self,mem1,loc='USA'):
        self.mem1 = mem1
        self.loc = loc
    
    def family_mem(self):
        print('Karthik Family Created, the members are {}'.format(self.mem1))

    def location(self):
        print(f'Karthik {self.surname} family lives in {self.loc}')

class Nive(Family):

    def __init__(self,mem1,loc='USA'):
        self.mem1 = mem1
        self.loc = loc
    
    def family_mem(self):
        print('Nive Family Created, the members are {}'.format(self.mem1))

    def location(self):
        print(f'Nive {self.surname} family lives in {self.loc}') 

manju = Family()
kn = Kirubahar('Viji','Shastika')
njk = Karthik('Pradeena')
nv = Nive('Madhu')

## All these objects can be called individually as below or via a for loop as below 
# print(kn.surname)
# kn.your_family()
# kn.family_mem()
# kn.location()
# print("\n")
# print("\n")


# print(njk.surname)
# njk.your_family()
# njk.family_mem()
# njk.location()
# print("\n")
# print("\n")

# print(nv.surname)
# nv.your_family()
# nv.family_mem()
# nv.location()
# print("\n")
# print("\n")


for member in [kn,njk,nv]:
    print(member.surname)
    member.your_family()
    member.family_mem()
    member.location()
    print("\n")

print(manju.surname)
manju.your_family()
manju.family_mem()


