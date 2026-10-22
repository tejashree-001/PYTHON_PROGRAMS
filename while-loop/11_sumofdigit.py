# Write a Python program to find the sum of digits of a given number

n = int(input("Enter a number: "))
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

print("Sum of digits is", sum)
