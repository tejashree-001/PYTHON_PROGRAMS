# Write a PYTHON program to print the multiplication table

n=int(input("Enter a number : "))

i=1
ans=0

while i<=10:
    ans=n*i
    print(n, "x" ,i,"=",ans)
    i=i+1
