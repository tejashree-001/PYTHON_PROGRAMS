
student = ['tejashree', 'sanskruti', 'apeksha', 'nidhi', 'sakshi']

while True:
    print("\nStudent Attendance Menu")
    print("1. Display total students present")
    print("2. Search student attendance")
    print("3. Add a new student")
    print("4. Remove an absent student")
    print("5. Display all students")
    print("6. Exit")

    choice = int(input("Enter a choice: "))

    if choice == 1:
        print("Total students present:", len(student))

    elif choice == 2:
        name = input("Enter student name to search: ").lower()

        if name in student:
            print(name, "is present in class.")
        else:
            print(name, "is not present in class.")

    elif choice == 3:
        name = input("Enter the new student's name: ").lower()

        if name not in student:
            student.append(name)
            print(name, "has been added successfully.")
        else:
            print(name, "is already in the attendance list.")

    elif choice == 4:
        name = input("Enter the absent student's name to remove: ").lower()

        if name in student:
            student.remove(name)
            print(name, "has been removed successfully.")
        else:
            print(name, "is not present in the list.")

    elif choice == 5:
        print("Students present in class:")
        for name in student:
            print(name)

    elif choice == 6:
        print("Exiting the attendance system.")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 6.")
