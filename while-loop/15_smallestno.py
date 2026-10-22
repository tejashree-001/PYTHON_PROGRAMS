# Write a PYTHON program to print smallest of n numbers


n=int(input("Enter a number that how much no you eill take:"))

i=1
smallest=int(input("enter a number 1 :"))

while i < n:
    num=int(input("Enter a number:"))
    

    if num<smallest:
        smallest=num
    i=i+1


print("smallest number is: ",smallest)