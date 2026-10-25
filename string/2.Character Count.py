# 2.Character Count 
# Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 



s = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in s:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == ' ':
        spaces += 1
    else:
        special += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Number of digits:", digits)
print("Number of spaces:", spaces)
print("Number of special characters:", special)
