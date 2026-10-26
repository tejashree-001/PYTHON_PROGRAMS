#14. Create a list containing duplicate values and display only unique elements.

list=[1,2,2,3,4,5,6,4,5]

new_list=[]

for i in list:
    if i not in new_list:
        new_list.append(i)


print("original list: ",list)

print("new list:",new_list)
        