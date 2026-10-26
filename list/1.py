#Write a Python program to create a list of five fruits and display the list.

fruits=[]

for i in range(5):
    fruit=input("Enter a fruit name: ")
    fruits.append(fruit)

print("list of fruit are:",fruits)