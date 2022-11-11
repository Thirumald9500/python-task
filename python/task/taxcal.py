import json
from turtle import position
f=open('data.json')
data=json.load(f)
# customername=input("enter the customer name : ")
# for i in data:
#     if i['CustomerName']==customername:
#         print('tax Percentage',i['TaxPercentage'],'% ')
#         print('Tax Amount',i['TaxAmount'])
lst1=[]
lst2=[]
for i in data:
    if i['TaxPercentage'] not in lst1:
        lst1.append(i['TaxPercentage'] )
        lst2.append(i['TaxAmount'])
    else:
        position=lst1.index(i['TaxPercentage'])
        temp=lst2.pop(position)
        lst2.insert(position,temp+i['TaxAmount'])
for i,j in zip(lst1,lst2):
    print(i,'% ',j)