password = input("Enter Your Password: ")
if not password.isalpha() and not password.isdigit() and len(password)>=8:
    print("Strong Password")
else:
    print("Weak Password")
    
    ###* not only alpha or not only digit