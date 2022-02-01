# The __init__ method is called as constructor method, which is a way to tell python to execute the code under it when an object of that class is created	
# If use case requires us to execute a set of code when the class object is created, then we could make use of the __init__ method.

# The __init__ method cannot be called manually, but is run implicitly 
# if the __init__ method is designed to accept a argument as (self, argument1) , then one positional argument needs to be passed when the class object is created as below,

# Incase if we don't have any mandatory code to be executed during the class object creation 
# we could ignore __init__ method which will do nothing as seen in the below examples


class InitExample():
    def __init__(self, variable1):
        print(variable1)
    
    def method_of_class(self, var):
        self.var = var + 40
        print(f'Altered Variable value is {self.var}')

    

i = InitExample('Hello, I am printed Immediately as a part of the function call')
print(type(i))
i.method_of_class(40)



class NewInit():
    def method_of_class(self, var):
        self.var = var + 10
        print(f'Altered Variable value is {self.var}')


j = NewInit()
print(type(j))
j.method_of_class(10)