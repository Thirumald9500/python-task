# acces the data frpm json file by using python

import json
f=open('data.json')
data=json.load(f)
for i in data:
    print(i['Product'])
    print()
