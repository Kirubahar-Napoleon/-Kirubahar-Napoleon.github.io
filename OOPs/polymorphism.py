# Python is so flexible that it allows users to re-use the same method name in as many as classes they want 
# They all will work specific to that class as seen below and will not return any error,

class poly1():
    def __init__(self, variable1):
        print(variable1)
    
    def method_of_class(self, var):
        self.var = var + 40
        print(f'Altered Variable value is {self.var}')

    def newmethod(self):
        print('method of poly1')
    
i = poly1('Hello, I am printed Immediately as a part of the function call')
i.method_of_class(40)
i.newmethod()


class poly2():
    def method_of_class(self, var):
        self.var = var + 10
        print(f'Altered Variable value is {self.var}')
    
    def newmethod(self):
        print('method of poly2')

j = poly2()
j.method_of_class(10)
j.newmethod()