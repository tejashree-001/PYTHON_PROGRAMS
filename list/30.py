
names = []
ages = []

n = int(input("Enter number of patients: "))

for i in range(n):
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))

    names.append(name)
    ages.append(age)

while True:
    print("\n1. Add a patient")
    print("2. Delete a patient")
    print("3. Search a patient")
    print("4. Display all patients")
    print("5. Count total patients")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))

        names.append(name)
        ages.append(age)

        print("Patient added successfully.")

    elif choice == 2:
        name = input("Enter patient name to delete: ")

        if name in names:
            index = names.index(name)
            names.pop(index)
            ages.pop(index)
            print("Patient deleted successfully.")
        else:
            print("Patient not found.")

    elif choice == 3:
        name = input("Enter patient name to search: ")

        if name in names:
            index = names.index(name)
            print("Patient name:", names[index])
            print("Patient age:", ages[index])
        else:
            print("Patient not found.")

    elif choice == 4:
        if len(names) == 0:
            print("No patients available.")
        else:
            print("\nPatient Details:")

            for i in range(len(names)):
                print("Name:", names[i], "| Age:", ages[i])

    elif choice == 5:
        print("Total patients:", len(names))

    elif choice == 6:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")