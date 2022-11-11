
# print('1 : addition')
# print('2 : subraction')
# print('3 : multiplication')
# print('4 : division')
# choice=int(input('Enter the choice : '))
# if choice==1:
#     a,b=map(int,input('enter the nums :').split())
#     print(a+b)
# elif choice==2:
#     a,b=map(int,input('enter the nums :').split())
#     print(a-b)
# elif choice==3:
#     a,b=map(int,input('enter the nums :').split())
#     print(a*b)
# elif choice==4:
#     a,b=map(int,input('enter the nums :').split())
#     print(a/b)
# else:
#     print('you entered an in valid choice')


a,b=map(int,input('enter the nums :').split())
print('1 : addition')
print('2 : subraction')
print('3 : multiplication')
print('4 : division')
print('5 : modules')
choice=int(input('Enter the choice : '))
if choice==1:   
    print("Addition : ",a+b)
elif choice==2:
    print("Subtraction : ",a-b)
elif choice==3:
    print("Multiplication : ",a*b)
elif choice==4:
    print("Division : ",a/b)
elif choice==5:
    print("Modulus : ",a%b)
else:
    print('you entered an in valid choice')

