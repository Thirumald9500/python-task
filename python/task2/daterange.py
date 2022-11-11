from datetime import date
lst=list(map(int,input('ENTER IN FORMAT DD/MM/YEAR\n').split('/')))
input_date = date(lst[2], lst[1],lst[0])
today_date=date.today()
difference=today_date-input_date
print(date.today())
print('the difference between the two date :',difference.days)