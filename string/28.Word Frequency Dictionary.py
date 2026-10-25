#Word Frequency Dictionary

s = input("Enter a paragraph: ").lower()

words = s.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)