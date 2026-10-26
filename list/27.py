
temperatures = []

for i in range(30):
    temp = float(input("Enter temperature of day " + str(i + 1) + ": "))
    temperatures.append(temp)

hottest = max(temperatures)
coldest = min(temperatures)
average = sum(temperatures) / len(temperatures)

print("\nHottest temperature:", hottest)
print("Hottest day:", temperatures.index(hottest) + 1)

print("Coldest temperature:", coldest)
print("Coldest day:", temperatures.index(coldest) + 1)

print("Average temperature:", round(average, 2))

print("\nDays above average temperature:")
for i in range(30):
    if temperatures[i] > average:
        print("Day", i + 1, ":", temperatures[i])

print("\nDays below average temperature:")
for i in range(30):
    if temperatures[i] < average:
        print("Day", i + 1, ":", temperatures[i])
