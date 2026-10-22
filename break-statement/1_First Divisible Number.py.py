# Write a Python program to print numbers from 1 to n. Stop the loop immediately when you find the first number divisible by both 3 and 7. Do not print that number.

n=int(input("Enter a number: "))

for i in range(1,n+1):
    print(i)
    if(i%3==0 and i%7==0):
        break

print("completed")
