'''
This is a test script
'''
class poly1():
    '''
    This class is now added with docstring
    '''
    def method_of_class(self, var):
        '''
        docstring for this method
        '''
        self.var = var + 40
        print(f'Altered Variable value is {self.var}')
    def newmethod(self):
        '''
        doc string for this newmethod
        '''
        print('method of poly1')
#function calls are made here
i = poly1()
i.method_of_class(40)
i.newmethod()