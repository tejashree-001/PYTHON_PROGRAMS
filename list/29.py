
scores = []

for i in range(10):
    score = int(input("Enter score in match: "))
    scores.append(score)

highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / len(scores)

centuries = 0
half_centuries = 0

for score in scores:
    if score >= 100:
        centuries += 1
    elif score >= 50 and score <= 99:
        half_centuries += 1

print("\nHighest score:", highest)
print("Lowest score:", lowest)
print("Total runs:", total)
print("Average runs:", round(average, 2))
print("Number of centuries:", centuries)
print("Number of half-centuries:", half_centuries)
