# Here we could import the functions from the other .py script and does not have to re-write the code exclusively
# to demonstrate how imports work, I am importing just one specific function of the mymod file
# But importing the other .py script "myanothermod" as module as whole

from mymod import mod_func
import myanothermod

#I am going to call the functions nows
#Here mod_func() and newfunc() are inside the mymod.py file and func2() and func3() functions are in myanothermod.py script
# Since we called the mod_func() exclusively on the import call of mymod, see how we call them as compared to the functions of the other module

mod_func()
myanothermod.func2()
myanothermod.func3()

# But the catch here is, we have only imported a speficic function called mod_func() of mymod.py file
# but this file has two functions, now lets try to call the other function and see what happens

newfunc()