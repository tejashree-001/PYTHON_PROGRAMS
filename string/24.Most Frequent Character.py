#24.Most Frequent Character 
#Find the character with the highest frequency. 

s=input("Enter a string: ")
max_count=0

result=""

for ch in s:
    count=s.count(ch)
    if count>max_count:
        max_count=count
        result=ch

print("most frequent char:", result)

print("frequency:",max_count)



