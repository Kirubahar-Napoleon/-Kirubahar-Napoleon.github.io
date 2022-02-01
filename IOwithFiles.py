# I have created a text file with name text.txt with below content 
# 1. Kirubahar Napoleon in first line
# 2. Viji in second line
# 3. Shasti kutty in third line
# 4. myfamily in fourth line

#I am now opening the text file into my varoable file1
file1 = open('/Users/kirubaha/Desktop/Python/text.txt')

#Printing file1 
print(file1.read())

#File reads use cursor based location, that is it readds from postition 0 and reads until last line, 
# when we read the file last time in file1 variable, the cursor already moved to last index, 
# now reading it again will not produce any output as below

print(file1.read())

#To be able to read it again we need to reset the cursor to index 0 as below
file1.seek(0)

#Now reading it again will produce a output 
print(file1.read())

#We can also reading from a specific index as below 
file1.seek(3)
print(file1.read())

#we can also read the files into a list as below using readlines, where each line becomes a value in list
file1.seek(0)
mylist = file1.readlines()
print(mylist)

#now we could print each item using its index in list as below
print('printing the second line of the file {}'.format(mylist[1]))
print('printing the third line of the file {}'.format(mylist[2]))
print('printing the first line of the file {}'.format(mylist[0]))

#The Python will hold onto the file it has read, so if another operation tries to delete that file it will return an error as file is open in python
#After using a file in python, it is always a best practice to close it, so that others can access it 
#to close the file use

file1.close()

#The Best way to open a file and use in python is using with as below,
#This will automatically read the file and assign its value to a variable and close it in the backend
#This way we dont have to worry about closing the file

with open('/Users/kirubaha/Desktop/Python/text.txt') as file2 :
    contents = file2.read()
    print(contents)

#By default the built-in open method opens a file in read mode, however it also supports other mode that allows us to write to the file as below
#Now lets try to open the file in different modes

with open('/Users/kirubaha/Desktop/Python/text.txt', mode='a') as f:
    f.write('\n5. fifth line is a new entry to family')

with open('/Users/kirubaha/Desktop/Python/text.txt', mode = 'r') as f2 :
    print(f2.read())

#When using write mode, it creates a file if that file name doesnot exist

with open('/Users/kirubaha/Desktop/Python/sfsdfd.txt', mode ='w') as w:
    w.write('I created this new file')

with open('/Users/kirubaha/Desktop/Python/sfsdfd.txt', mode ='r') as r:
    print(r.read())

