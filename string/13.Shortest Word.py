#13.Shortest Word 




s = input("Enter a sentence: ")

words = s.split()
small= words[0]

for word in words:
    if len(word) < len(small):
        small = word

print("smallest word is:", small)
print("Length of small word:", len(small))
