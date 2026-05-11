age = input("Enter age:")
country = input("Enter country:").title()

if age.isdigit():
    age = int(age)
    if age >= 18 or country == "Japan" :
        print("Access Granted")
    else:
        print("Access Denied")