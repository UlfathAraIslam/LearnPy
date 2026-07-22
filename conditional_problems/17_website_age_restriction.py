age = input("Enter age:")
if age.isdigit():
    age = int(age)
    if age >= 13:
        print("Account creation allowed")
    else:
        print("Account creation denied")
else:
    print("invalid age")