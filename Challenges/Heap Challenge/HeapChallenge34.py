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
import requests
import time
from datetime import datetime

url = "https://hooks.chime.aws/incomingwebhooks/5b0ebbbc-ec22-4cc8-b3b4-b9b4f532b445?token=VjFTTERMVTZ8MXx1ekRBZHNvN1pROFE3d1VXSzM1NVJzWi1tTF81Q0ZhUVpLdS1abVdkMHE0"
msg = {}

for key,value in mydict.items():
    msgtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg["Content"] = str(f'The {key} has been working with the Heap team for {value} days. This message was generated at {msgtime}')
    msgdata = json.dumps(msg)
    chimemsg = requests.post(url, data=msgdata)
    print(chimemsg.text)
    print('waiting for 2 sec')
    time.sleep(2)