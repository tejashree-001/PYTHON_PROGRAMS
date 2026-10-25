# Remove Spaces 

s=input("Enter a string:")

str=""

for ch in s:
    if ch!=" ":
        str=str+ch

print(s)
print(str)