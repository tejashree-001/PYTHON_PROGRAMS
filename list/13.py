# Accept 10 numbers and sort them in:
#Ascending order
# Descending order

num=[]

for i in range(10):
    n=int(input("Enter a number:"))
    num.append(n)

num.sort()
print("ascending order",num)

num.sort(reverse=True)
print("descending order",num)