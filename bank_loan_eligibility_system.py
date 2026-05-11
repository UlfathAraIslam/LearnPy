salary = input("Enter salary:")
experience =  input("Enter experience:")

if salary.isdigit() and experience.isdigit():
    salary= int(salary)
    experience = int(experience)
    if salary >= 300000 and experience >= 2:
        print("Loan Approved")
    elif salary < 300000:
        print("Salary requirement not met")
    elif experience < 2:
        print("Experience requirement not met")
    else:
        print("Loan is not approved")
else:
    print("Enter valid numbers")