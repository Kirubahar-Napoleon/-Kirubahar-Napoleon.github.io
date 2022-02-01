#we could use *args which allows us to take as many as variables as tuples as below
def my5percent (*args):
    print(args)
    return sum ((args)) * 0.05
    
print(my5percent(10,20,30,40,50,60))
print(my5percent(10,20,30,40,50,60,70))


#The word args is not necessarily need to be "args" it can be anything as below, and they have same effect, However it is best practice to use args to let the user who reads the function that it is "args" by convention.

def my5percent (*MyManyArgument):
    print(MyManyArgument)
    return sum ((MyManyArgument)) * 0.05
    
print(my5percent(10,20,30,40,50,60))
print(my5percent(10,20,30,40,50,60,70))



#Like how args allows us to pass many values to the function, kwargs allows us to pass many named values/arguments (i.e) each argument is represented by a name to the function, where we are unsure the number of such inputs
#To tell the function that it is a kwargs we need to define it with two asterix as ** as below,

def myfunc(**kwargs):
    print(kwargs)
    for key,values in kwargs.items():
        print(key)
        print(values)

myfunc(Name='Kirubahar', Age='30', height='6ft', gender='Male')


def mydict(**kwargs):
    print(kwargs)
    print(list(kwargs.keys()))
    print(list(kwargs.values()))

mydict(Name='Kirubahar', Age='30', height='6ft', gender='Male')


#As with the case of args, kwargs can also be represented by any argument name apart from kwargs. As long as the argument is passed with ** , 
# The function will understand it, but it is best practice to use kwargs for better understanding and reading

def AgeFinder(**person):
    if 'Age' in person:
        if int(person['Age']) >= 25:
            print('The Person is allowed for the vaccine')
        else:
            print('The person is underage to be allowed to get the vaccine')
    else:
        print('No agen details found, this Person can be rejected due to lack of data')

AgeFinder(Name='Kirubahar', Age='30', height='6ft', gender='Male')


#We could also pass both args and kwargs to the same function and they would still work without issues as below,

def complex(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like to order {} {} for starters'.format(args[1],kwargs['food']))

complex(10,2,3,4,5,6,9,Veg='Carrots',food='Chicken Soup',fruit='Apple')
