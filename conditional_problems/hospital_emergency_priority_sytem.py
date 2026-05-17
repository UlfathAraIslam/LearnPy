age = input("Enter age:")
emergency_level = input("Enter emergency level:")

if age.isdigit() and emergency_level.isdigit():
    age = int(age)
    emergency_level = int(emergency_level)
    if age >= 60 or emergency_level >= 7:
        print("Priority Treatment")
    elif age >=18 and emergency_level >=4:
        print("Normal Treatment")
    else:
        print("Standard Queue")
else:
    print("Enter valid numbers")