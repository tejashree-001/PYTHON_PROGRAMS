#8.Frequency of a Character 
#Find the number of times a specified character appears in a string. 

s= input("Enter a string: ")

char=input("Enter a charter to check frequency: ")
count=0
for ch in s:
    if ch==char:
        count=count+1

print("the frequency of the char is ",count)