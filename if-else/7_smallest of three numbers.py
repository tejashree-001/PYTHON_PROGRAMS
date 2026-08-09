# Write a PYTHON program to find smallest of three numbers

a,b,c=map(int,input("Enter three numbers: ").split())
if a<b and a<c:
    print(a,"is the smallest number.")
elif b<a and b<c:
    print(b,"is the smallest number.")
else:
    print(c,"is the smallest number.")


# method 2
# using min function

a,b,c=map(int,input("enter three numbers:").split())
smallest = min(a,b,c)
print("smallest number is :",smallest)
