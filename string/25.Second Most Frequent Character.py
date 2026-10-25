#25.Second Most Frequent Character 

s = input("Enter a string: ")

first = 0
second = 0
result = ""

for ch in s:
    count = s.count(ch)

    if count > first:
        second = first
        first = count
    elif count > second and count < first:
        second = count

for ch in s:
    if s.count(ch) == second:
        result = ch
        break

print("Second most frequent character:", result)
print("Frequency:", second)