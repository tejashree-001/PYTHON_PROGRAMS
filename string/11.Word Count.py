# 11.Word Count 
s=input("Enter a string:")

count=0

for ch in s:
    if ch !=" ":
        count=count+1

print(s)
print("the word count is:",count)