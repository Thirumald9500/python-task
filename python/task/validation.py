import json,re
f=open('data.json')
data=json.load(f)
for i in data:
    mobilenum=str(i['ContactNo'])
    if len(mobilenum)==10 and int(mobilenum[0]) in range(6,10) and mobilenum.isnumeric(): 
        continue
    else:
        print(i['CustomerName'], i['ContactNo'] )
    email=i['EmailID']
    if len(email)>11 and ('@gmail.com' or '@yahoo.com') in email :
        continue
    else:
        print('not valid mail',i['EmailID'])





        # print(email)
    # regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # if(re.fullmatch(regex, email)):
    #     continue
    # else:
    #     print(i['CustomerName'], i['EmailID'])
            # checks lenth and first num between 6-9 and all are numbers
    #     print(i['CustomerName'])
    # Pattern = re.compile("(0|91)?[6-9][0-9]{9}")"{6,9}[2]{0,9}[8]"
    # if Pattern.match(mobilenum):