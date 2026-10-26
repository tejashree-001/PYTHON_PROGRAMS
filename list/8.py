#Store 15 integers in a list. Count howmany numbers are:even #odd

```python
numbers = []
even = []
odd = []

for i in range(15):
    n = int(input("Enter a number: "))
    numbers.append(n)

    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("List is:", numbers)
print("Even numbers are:", even)
print("Odd numbers are:", odd)

print("Count of even numbers:", len(even))
print("Count of odd numbers:", len(odd))
```