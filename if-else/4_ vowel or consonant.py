#Write a PYTHON program to check entered character is vowel or consonant.

char=input("Enter any charcter from(a-z):")
if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
    print("Entered charcter is vowel.")
else:
    print("Entered charcter is consonant.")


# method 2

char=input("Enter a charcter from (a-z):")
if char in "aeiouAEIOU":
    print("charcter is vowel.")
else:
    print("charcter is consonant.")
    

#method 3

char = input("Enter a character: ")

if char.lower() in "aeiou":
    print(char, "is a vowel")
else:
    print(char, "is a consonant")    
