import json
f=open('data.json')
data1=json.load(f)
odernum=int(input('---> Enter the oder num : '))
for i in data1:
  if i['OrderNo'] == odernum:
    print('*'*50)
    print('\t\t  YOUR BILL')
    print('='*50)
    print('\tCustomerName    :',i['CustomerName'])
    print('\tContactNo       :',i['ContactNo']) 
    print('\tOrderDate       :',i['OrderDate'])
    for j in i['Product']:
      print('\tProductName     :',j['Name'])
      print('\tQty             :',j['Qty']) 
      print('\tRate            :',j['Rate'])  
    print('\tOrderValue      :',i['OrderValue']) 
    print('=' * 50)
    print('\tTaxPercentage :',i['TaxPercentage']) 
    print('\tTaxAmount     :',i['TaxAmount']) 
    print('\tNetAmount     :',i['NetAmount'])
    print('*'*50)
    print('\t\t  THANK YOU')
    print('*'*50)




            