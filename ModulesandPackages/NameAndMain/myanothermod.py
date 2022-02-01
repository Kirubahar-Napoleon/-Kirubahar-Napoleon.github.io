print('I am also a Module')

def func2():
    print('I am  func2() function inside the myanothermod.py script')

def func3():
    print('I am  func3() function inside the myanothermod.py script')

if __name__ != '__main__':
    print('I am being imported')
    func2()
    func3()