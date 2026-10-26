#Rotate a list:
# Left by one position
# Right by one position


numbers = [10, 20, 30, 40, 50]

first = numbers.pop(0)
numbers.append(first)

print("Left rotated list:", numbers)



numbers = [10, 20, 30, 40, 50]

last = numbers.pop()
numbers.insert(0, last)

print("Right rotated list:", numbers)
