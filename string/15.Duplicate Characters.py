# 15.Duplicate Characters 

s=input("Enter a string:")

for ch in s:
    if s.count(ch)>1 and ch not in s[:s.index(ch)]:
        print(ch,end=" ")

