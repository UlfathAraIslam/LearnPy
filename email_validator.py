email = input("Enter email:")

if "@" in email and email.endswith(".com"):
    print("Valid Email")
else:
    print("Invalid Email")