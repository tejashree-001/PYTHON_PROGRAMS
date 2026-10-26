

salaries = []

n = int(input("Enter number of employees: "))

for i in range(n):
    salary = float(input("Enter salary of employee: ₹"))
    salaries.append(salary)

highest = max(salaries)
lowest = min(salaries)
average = sum(salaries) / len(salaries)

above = 0
below = 0

for salary in salaries:
    if salary > 50000:
        above += 1

    if salary < 30000:
        below += 1

print("\nHighest salary: ₹", highest)
print("Lowest salary: ₹", lowest)
print("Average salary: ₹", round(average, 2))
print("Employees earning above ₹50,000:", above)
print("Employees earning below ₹30,000:", below)