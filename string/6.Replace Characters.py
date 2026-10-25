#6.Replace Characters 
#Replace all occurrences of a given character with another character. 

s=input("Enter a string:")

old=input("Enter a char to replace:")
new=input("Enter a char which replace these old char:")

string=""

for ch in s:
    if ch==old:
        string=string+new
    else:
        string=string+ch

print("the old string is:",s)
print("the new string is:",string)
        