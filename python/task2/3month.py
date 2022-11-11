
from datetime import date
from dateutil.relativedelta import relativedelta
y,m,d = map(int,input("yyyy,mm,dd : ").split('.'))
current_date = date(year=y,month=m,day=d)
past_date = current_date - relativedelta(months=3)
print(past_date)


#emidate

# dayw = current_date+relativedelta(months=+1)
# print(dayw.weekday())
# if dayw.weekday() is 5:print(dayw-relativedelta(days=1))
# print(dayw,dayw.weekday(),type(dayw))

