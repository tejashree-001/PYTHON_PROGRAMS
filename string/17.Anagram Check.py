#17.Anagram Check 

s1=input("Enter a string:")

s2=input("Enter a sting: ")

if sorted(s1)==sorted(s2):
    print("this are the anagram.")
else:
    print("not anagram")