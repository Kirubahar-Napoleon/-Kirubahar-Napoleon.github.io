# We all come across errors in our code. 
# In Python, when an error or exception occurs, the code will stop executing
# However at times we would want our code to execute some block of code always despite there is a error or not
# We could achieve this by using try, except, else and finally 
	
# Try - any block of code inside a try block will be tried to execute by python
# Except : If there is any error in executing the code block inside the try, the except block will run
# Else : the else is used in con-junction with try and except, where we say python to run the cpde inside the elese block, if there is no error occurred while trying the try block

# Finally : Finally code block tell python to always run the set of code inside it, despite an error occurred or not.


# Note : Except can be defined as just "except : " 
# When this is done, the code block inside it will be executed no matter what exception occurs
# However we could also run actions specific to the type of execution occurred, like NotImplementedError, TypeError, OSError etc,
# List of Built in Exceptions can be found here - https://docs.python.org/3/library/exceptions.html


try :
    #we are opening a new text file in write mode
    f = open('testfile.txt','w')
    f.write('Test write this to the file')
    f.close()
    #again we could open a new file in read mode that does nto exist, this should thrown an exception
    f1 = open('newtestfile.txt','r')
    print(f1.read())
except IOError:
    # This will only check for an IOError exception and then execute this print statement
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()
finally:
    #to show that the first write operation did not cause the error we will open it here in read block
    #As we know finally block will always run no matter what
    f1 = open('testfile.txt','r')
    print(f1.read())


#To demonstrate Else block we could run below code

Total = lambda a,b : a + b

while True:
    try:
        num1 = 10
        num2 = int(input('Please enter a number:'))
        print(Total(num1,num2))
    except :
        print('The input provided is not a valid Integer')
        continue
    else :
        print('Thanks for using our service')
        break



