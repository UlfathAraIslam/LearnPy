skill = input("Enter skill level(beginner/intermediate/advance):").lower()
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
else:
    print("Invalid number")