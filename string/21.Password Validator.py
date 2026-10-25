#21.Password Validator


s=input("Enter a password:")


upper = False
lower = False
digit = False
special = False


for ch in s:
    if ch.isupper():
        upper=True
    elif ch.islower():
        lower=True
    elif ch.isdigit():
        digit=True
    else:
        special=True
       
if len(s)>8 and upper and lower and digit and special:
    print("valid",s)
else:
    print("invalid")
