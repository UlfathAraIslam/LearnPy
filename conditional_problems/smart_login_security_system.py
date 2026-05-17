username = input("Enter username:").lower()
password = input("Enter password:")
otp = input("Enter OTP:")

if password.isdigit() and otp.isdigit():

    password = int(password)
    otp = int(otp)

    if username == "admin" and password == 12345 and otp == 9999:
        print ("Login Approved")
    elif username != "admin":
        print ("Invalid Username")
    elif password != 12345:
        print ("Wrong Password")
    elif otp != 9999:
        print ("Invalid OTP")
else:
    print("Password and OTP must be numbers")