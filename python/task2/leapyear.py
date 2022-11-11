year=int(input())

if year%4 ==0 :
    if year%100 != 0 or year%400 == 0:
        print("leap year")
    else:
        print("not leap year")
else:
    print("not a leap year")
print(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

#4,8,12,16.....100,104,108...400