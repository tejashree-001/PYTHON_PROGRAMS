#Create a shopping cart using a list.
#Perform:
# Add item
# Remove item
# Search item
# Display cart
# Count total items

cart = []

while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. Search item")
    print("4. Display cart")
    print("5. Count total items")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item to add: ")
        cart.append(item)
        print(item, "added to cart.")
        print(cart)
    elif choice == 2:
        item = input("Enter item to remove: ")

        if item in cart:
            cart.remove(item)
            print(item, "removed from cart.")
        else:
            print("Item not found in cart.")

    elif choice == 3:
        item = input("Enter item to search: ")

        if item in cart:
            print(item, "is available in the cart.")
        else:
            print(item, "is not available in the cart.")

    elif choice == 4:
        print("Shopping cart:", cart)

    elif choice == 5:
        print("Total items in cart:", len(cart))

    elif choice == 6:
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice. Please try again.")

