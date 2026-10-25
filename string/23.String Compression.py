#23.String Compression 
#Compress repeated characters and return the original string if compression does not reduce #the length. 


s=input("Enter a string: ")

result=""
count=1

for i in range(1,len(s)):
    if[s]==s[i-1]:
        count+=1
    else:
        result=result+s[i-1]+str(count)
        count=1

if len(s)>0:
    result+=s[i]+str(count)

if len(result)< len(s):
    print(result)
else:
    print(s)
