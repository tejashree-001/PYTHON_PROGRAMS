#5.Uppercase and Lowercase Count 
#Count the number of uppercase and lowercase letters in a string. 

s=input("Enter a string:")

low=0
up=0

for ch in s:
    if ch.islower():
        low=low+1
    elif ch.isupper():
        up=up+1

print("the no of lowercase is:",low)
print("the no of uppercase:",up)