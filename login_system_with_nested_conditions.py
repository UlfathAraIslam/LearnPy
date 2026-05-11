username = input("Enter username:")
password = int(input("Enter password:"))

if username == "admin":
    if password == 12345:
        print ("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")