skill = input("Enter skill level:").lower()
age = input("Enter age:")

if age.isdigit():
    age = int(age)
    if skill == "beginner" and age >= 18:
        print("Enrollment Approved")
    elif skill == "intermediate" and age >=16:
        print("Enrollment Approved")
    elif skill == "advanced" and age >=14:
        print("Enrollment Approved")
    elif age < 14:
        print("Enrollment Denied")
    elif skill not in ["beginner","intermediate","advanced"]:
        print("Invalid Input")
else:
    print("Invalid number")