#Create a list of cities. Ask the user to enter a city name #and checkwhether it exists in the list.


list=['kolahpur','pune','vashi','basarge','miraj']

city=input("Enter a city to find:")

for i in list:
    if city  in list:
        exist=True

    else:
        exist=False


if exist==True:
    print("exist")
else:
    print("not exist")