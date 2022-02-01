# All methods inside the python class needs to have at least one argument called self
# This self argument tells python that it is referring to itself
# If this is not passed, python do not know what it has to do with that method as seen below,


class SelfExample():
    def __init__(self, variable1):
        self.variable1 = variable1
        print(f'{variable1} is same as {self.variable1}')

    
    def method_of_class():
        print('Nothing to print here under method_of_class')

    def new_method(self):
        print('Nothing to print here under new_method')

i = SelfExample(10)
i.new_method()
i.method_of_class()


# As we could see here, though we did not send any argument when calling the method_of_class method, 
# However python says it is passed with 1. This is from the class itself implicitly. 
# To accept this method call, we need to pass a self keyword which will solve this issue
# It is required to pass the self argument in additon to other positional argument if any

#To fix the above code, just add self argument to the method_of_class() as below
## Please note below code will not execute unless the above code block related to SelfExample class is corrected

class SelfExample1():
    def __init__(self, variable1):
        self.variable1 = variable1
        print(f'{variable1} is same as {self.variable1}')

    
    def method_of_class(self):
        print('Nothing to print here under method_of_class')

    def new_method(self):
        print('Nothing to print here under new_method')

j = SelfExample1(10)
j.new_method()
j.method_of_class()