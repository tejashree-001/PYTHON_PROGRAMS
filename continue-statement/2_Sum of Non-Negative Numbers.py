#Sum of Non-Negative Numbers


n = int(input("How many numbers do you want to enter? "))

total = 0
count = 0

for i in range(n):
    num = int(input("Enter a number: "))

    if num < 0:
        continue

    total = total + num
    count = count + 1

print("Sum of non-negative numbers:", total)
print("Count of non-negative numbers:", count)