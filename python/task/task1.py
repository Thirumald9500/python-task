import json
f=open('data.json')
data=json.load(f)
costmername=[]
cont=[]
for i in data:
# condition checks name in new customername list
    if i['CustomerName'] not in costmername: 
        costmername.append(i['CustomerName'])
        cont.append(costmername.count(i['CustomerName']))

    else:
        position=costmername.index(i['CustomerName'])
        var=cont.pop(position)
        cont.insert(position,var+1)
for i,j in zip(costmername,cont):
    print(i,j,'orders')
            
