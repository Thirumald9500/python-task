# march31-april1
y,m,d = map(int,input("yyyy,mm,dd : ").split('.'))
if m in range(4,12):
    print(y+1)
else:
    print(y)
