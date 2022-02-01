import json

mystring = str("""| user1 | 6 |
| user2 | 9 |
| user3 | 15 |""")

mydict = {}

#Manipulating stirng to remove pipes and then splitting the resulting string based on line breaks to make it a list
mystring =  mystring.replace('| ','').replace(' |','')
mydelimitedlist = mystring.splitlines()

#Iterating through list to assign values to dict
for mem in mydelimitedlist:
    mem = mem.split(' ')
    mydict[mem[0]] = int(mem[1])

#Converting dict into json for pretty printing
myjson = json.dumps(mydict, indent=3)
print(myjson)


#Challenge 4
#Need webhook access to get it to work