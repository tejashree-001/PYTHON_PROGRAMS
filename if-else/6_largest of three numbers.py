# Write a PYTHON program to find largest of three numbers.

a,b,c=map(int,input("Enter three numbers: ").split())
if a>b and a>c:
    print(a,"is the largest number.")
elif b>a and b>c:
    print(b,"is the largest number.")
else:
    print(c,"is the largest number.")


# method 2
# using max function

a,b,c=map(int,input("enter three numbers:").split())
largest = max(a,b,c)
print("largest number is :",largest)
