#Create a list of books.
#Implement:
# Add a new book
# Search a book
# Remove a book
# Display all books
# Count total books

books=["c programming","python","java","c++"]

books.append('r programming')
books.pop(3)

name=input("Enter a name of book to search:")

if name in books:
    print("Search sussfully")
else:
    print("search unsussesful ")

print("all books are:",books)

print("total count of books:",len(books))



