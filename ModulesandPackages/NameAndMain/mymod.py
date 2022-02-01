print('I am a Module')

def mod_func():
    print('I am  mod_func() function inside the mymod.py script')

def newfunc():
    print('I am  newfunc() function inside the mymod.py script')

if __name__ == '__main__':
    print('I am being executed as standalone')
    mod_func()
    newfunc()
