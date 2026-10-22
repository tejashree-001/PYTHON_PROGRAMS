# Write a PYTHON program to check the entered  number is palindrome or not

n=int(input("Enter a number: "))

temp=n
rev=0


while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10

if temp==rev:
    print("The number is palindrome.")
else:
    print("the no is not palindrome")

