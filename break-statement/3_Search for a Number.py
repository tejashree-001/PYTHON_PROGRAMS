# Search for a Number

# Write a Python program that accepts n numbers and a target number. Search for the target using a loop. If the target is found, print its position and stop searching using break. If it is not found, display an appropriate message.


n = int(input("How many numbers do you want to enter: "))
target = int(input("Enter the target number: "))

i = 1
found = False

while i <= n:
    num = int(input("Enter a number: "))

    if num == target:
        print("Target found at position", i)
        found = True
        break

    i = i + 1

if found == False:
    print("Target not found")

