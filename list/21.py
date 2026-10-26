#Accept two lists and merge theminto a single list.

list1=[]
list2=[]

n1=int(input("Enter a elements in the first list:"))
for i in  range(n1):
    item=input("Enter a items in list1:")
    list1.append(item)

n2=int(input("Enter a elements in the second list2:"))
for i in range(n2):
    item=input("Enter a items in list2:")
    list2.append(item)

list3=list1+list2

print(list1)
print(list2)
print(list3)


# another method

list1=[1,2,3]
list2=[4,5,6]

list1.extend(list2)
print("merged list",list1)