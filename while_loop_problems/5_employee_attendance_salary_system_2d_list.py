#5
'''
-employees =[["Aiko Yamamoto",28,2000]["Kenji Mori",18,1500]["Hana Sato",22,1800]["Riku Tanaka",26,2500]]
-index= 0
-while loop
-Access values using records[i][0], records[i][1], records[i][2].
-salary- daily wage * days
-Deduct 10% from salary if days present is below 20.
-Add a 5% bonus if days present is 26 or more.
-Otherwise pay exact salary (days_present x daily_wage).
-Print a formatted payroll report for all employees.

'''
records = [
    ["Aiko Yamamoto", 28, 2000],
    ["Kenji Mori", 18, 1500],
    ["Hana Sato", 22, 1800],
    ["Riku Tanaka", 26, 2500]
]

i = 0
total_payroll = 0

print("=================================================")
print("MONTHLY PAYROLL REPORT")
print("=================================================")
print("Name | Days | Daily Wage | Salary | Status")
print("-------------------------------------------------")

while i < len(records):

    name = records[i][0]
    days_present = records[i][1]
    daily_wage = records[i][2]

    salary = days_present * daily_wage

    if days_present < 20:
        salary = salary - (salary * 0.10)
        status = "Deducted"

    elif days_present >= 26:
        salary = salary + (salary * 0.05)
        status = "Bonus"

    else:
        status = "Standard"

    total_payroll += salary

    print(
        f"{name.title()} | "
        f"{days_present} | "
        f"{daily_wage} | "
        f"{(salary)} | "
        f"{status}"
    )

    i += 1

print("-------------------------------------------------")
print(f"Total Payroll: {total_payroll}")