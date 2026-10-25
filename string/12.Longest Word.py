# 12.Longest Word 
#Find the longest word in a given sentence. 

# Longest Word

s = input("Enter a sentence: ")

words = s.split()
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word is:", longest)
print("Length of longest word:", len(longest))
