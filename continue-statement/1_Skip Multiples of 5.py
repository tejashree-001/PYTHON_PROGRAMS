#Skip Multiples of 5

# Write a Python program to print all numbers from 1 to n, skipping numbers that are divisible by 5. Use continue.

n=int(input("Enter a number: "))

for i in range(1,n+1):
    if(n%5==0):
        continue

    print(i)
    i=i+1

    