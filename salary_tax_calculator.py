salary = input("Enter salary:")

if salary.isdigit():
    salary = float(salary)
    if salary > 1000000:
        tax = salary * 0.3
        print("Tax",tax)
    elif salary > 500000:
        tax = salary * 0.1
        print("Tax",tax)
    else:
        print("No tax")
else:
    tax = "Tax:"
    print(tax)