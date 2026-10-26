#Write a program to find the largest and smallest number in a list without using max()
#or min().

list=[34,45,67,23,54,31]

largest=list[0]

for i in  list:
    if largest<i:
        largest=i


print(list)
    

print("the largest number is",largest)

smallest=list[0]

for i in list:
    if smallest>i:
        smallest=i


print("smallest no is :",smallest)
    
    