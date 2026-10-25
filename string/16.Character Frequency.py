#16.Character Frequency 

s=input("Enter a string:  ")

for ch in s:
    if ch not in s[:s.index(ch)]:
        print(ch,"=",s.count(ch))
    

