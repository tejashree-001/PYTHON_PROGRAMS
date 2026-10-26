#25.Remove all duplicate elements while preserving the original order.


numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print("Original list:", numbers)
print("List after removing duplicates:", unique)
