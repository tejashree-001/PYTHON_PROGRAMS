#Find Numbers with No Repeated Digits


n = int(input("Enter a number: "))

for i in range(1, n + 1):
    s = str(i)
    repeated = False

    for j in range(len(s)):
        if s.count(s[j]) > 1:
            repeated = True
            break

    if repeated:
        continue

    print(i, end=" ")
