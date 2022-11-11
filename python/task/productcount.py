import json
f=open('data.json')
data=json.load(f)
lst=[]
qty=[]
for i in data:
    for j in i['Product']:
        if j['Name'] not in lst:
            lst.append(j['Name'])
            qty.append(j['Qty'])
        else:
            position=lst.index(j['Name'])
            temp=qty.pop(position)
            qty.insert(position,temp+j['Qty'])
for i,j in zip(lst,qty):
    print(i,j,'qty')