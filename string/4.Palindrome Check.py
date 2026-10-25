# 4.Palindrome Check 

s=input("Enter a string: ")

rev=" "

for ch in s:
    rev=ch+rev

if s==rev:
    print("The string is palindrome")
else:
    print("The string is not palindrome")