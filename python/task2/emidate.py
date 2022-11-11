from datetime import date
from dateutil.relativedelta import relativedelta
y,m,d = map(int,input("yyyy,mm,dd : ").split('.'))
n_emi=int(input('Enter no of EMI : '))
current_date = date(year=y,month=m,day=d)

for i in range(n_emi):
    current_date=current_date + relativedelta(months=+1) 
    if current_date.weekday() ==  5: 
        # SATURDAY has been converterd to friday by using weekday()5-4
        print(current_date+relativedelta(days=-1))
    elif current_date.weekday() == 6:
        # Sunday has been converterd to monday by using weekday()6-0
        print(current_date+relativedelta(days=+1))
    else:
        print(current_date)

        