# usename and login check 


correct_username = "admin"
correct_password = "1234"

attempt = 1

while attempt <= 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Invalid username or password")

    attempt = attempt + 1

if attempt > 3:
    print("Account access denied")
