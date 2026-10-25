#27.Email Validator

s = input("Enter an email: ")

if "@" in s and "." in s and s.index("@") < s.rindex(".") and " " not in s:
    print("Valid Email")
else:
    print("Invalid Email")