#Print Numbers Not Divisible by 2 or 3


n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 2 == 0 or i % 3 == 0:
        continue

    print(i, end=" ")
