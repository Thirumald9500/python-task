# list1=[1,2,3,4,5,6]
# list2=[2,3,4,5,7,8,9]
# list1=set(list1)
# list2=set(list2)
# list3=[]
# for i in list1:
#     if i in list2:
#       list3.append(i)
# print(*list3)


set1=set(map(int,input().split()))
set2=set(map(int,input().split()))
print(set1.intersection(set2))