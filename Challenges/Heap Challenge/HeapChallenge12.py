#Input given
myinput_list = [2,'g',5,2,'k',1,'a',5,7,'o',9,8,'h',3,4,'e',4,10,'y']

#Creating two sets to segregate between str & int for sorting and also to prevent duplicates
mycharset = set()
mynumset = set()

for mem in myinput_list:
    #Performing check to determine type of list member
    if type(mem) == int :
        mynumset.add(int(mem))
    else:
        mycharset.add(str(mem))

#printing sorted set as list    
print('Output for challenge 1 is {}'.format(sorted(mynumset) + sorted(mycharset)))


#Line Break
print('\n')

#Challenge2 below which uses above output
#For this challenge no sets from the challenge 1 is used, a new iteration is performed again to segregate between str and int
#importing json function to print the resulting dictionary here

import json 
mynewlist = sorted(mynumset) + sorted(mycharset)
mynumlist = []
mystrlist = []
mydict = {}
total = 0

for mem in mynewlist:
    if type(mem) == int:
        mynumlist.append(int(mem))
        total += mem
    else:
        mystrlist.append(str(mem))

mydict["list"] = mynewlist
mydict["total"] = total
mydict["string_count"] = len(mystrlist)
mydict["integers"] = mynumlist
mydict["strings"] = mystrlist
myjson = json.dumps(mydict, indent=3)
print( f'json output for challenge 2 is {myjson}')