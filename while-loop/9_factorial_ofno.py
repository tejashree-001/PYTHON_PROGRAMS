#Write a PYTHON program  find a factorial of given number

n=int(input("Enter a number:"))
i=1
fact=1

while i<=n:
    fact=fact*i
    i=i+1

print("factorial is",fact)

