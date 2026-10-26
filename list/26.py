#Storemarks of 20 students in a list and determine:
# Highestmarks
# Lowestmarks
# Averagemarks
# Number of students scoring above average
#Number of students scoring belowaverage


marks = []

for i in range(20):
    m = float(input("Enter marks of student: "))
    marks.append(m)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

above = 0
below = 0

for i in marks:
    if i > average:
        above += 1
    elif i < average:
        below += 1

print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Students scoring above average:", above)
print("Students scoring below average:", below)
