# Write a PYTHON program that prints  1 2 4 8 16 32 … n2

num=int(input("Enter a number:"))
for i in range (num+1):
    print(2**i)
