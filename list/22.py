#Find common elements between two lists.


list1=[1,2,3,4,5]
list2=[1,4,3,6,7]

common=[]

for i in list1:
    if i in list2:
        common.append(i)

print("common elements:",common)