#Write a PYTHON program to print the largest of n numbers

n=int(input("Enter a number that how much no you eill take:"))

i=1
largest=int(input("enter a number 1 :"))

while i < n:
    num=int(input("Enter a number:"))
    

    if num>largest:
        largest=num
    i=i+1


print("largest number is: ",largest)