from datetime import date
d,m,y=map(int,input('ENTER IN FORMAT DD/MM/YEAR\n').split('/'))
print(date(y,m,d))