#Write a PYTHON program to check the entered number is prime or not


n=int(input("Enter a number: "))

i=1
count=0

while i<=n:
    if n%i==0:
        count=count+1
    i=i+1


if count==2:
    print("number is prime")
else:
    print("number is not prime")
