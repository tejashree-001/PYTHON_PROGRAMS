#Sum Until Zero

# Write a Python program that accepts integers continuously from the user. Stop taking input when the user enters 0. Display the sum and count of all numbers entered before 0.



total = 0
count = 0

while True:
    n = int(input("Enter a number: "))

    if n == 0:
        break

    total = total + n
    count = count + 1

print("Sum =", total)
print("Count =", count)
