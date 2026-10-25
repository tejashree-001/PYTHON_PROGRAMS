#Process Student Marks


n = int(input("Enter the number of students: "))

total = 0
count = 0
passed = 0
failed = 0

for i in range(n):
    marks = float(input("Enter marks: "))

    if marks < 0 or marks > 100:
        continue

    total = total + marks
    count = count + 1

    if marks >= 40:
        passed = passed + 1
    else:
        failed = failed + 1

print("Number of students passed:", passed)
print("Number of students failed:", failed)

if count > 0:
    average = total / count
    print("Average valid marks:", round(average, 2))
else:
    print("No valid marks entered.")
