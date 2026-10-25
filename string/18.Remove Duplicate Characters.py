#18.Remove Duplicate Characters 

s=input("Enter a string:")

temp=" "

for ch in s:
    if ch not in temp:
        temp=temp+ch


print(temp)