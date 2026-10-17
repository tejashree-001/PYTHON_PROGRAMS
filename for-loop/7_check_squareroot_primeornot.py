# check the given number square root is prime or not

n=int(input("Enter a number: "))

root=int(n**0.5)

if root*root==n and root>1:
    prime=True

    for i in range(2, root):
        if(root%i)==0:
            prime=False
            break

    if prime:
     print("The number is prime.")
    else:
     print("The number is not prime.")

else:
    print("The number is not prime.")
