# 2D list to store patients
patients = []

# Counters
priority_count = 0
normal_count = 0
standard_count = 0

while True:

    name = input("Enter patient name (or 'done'): ").title()

    if name.lower() == "done":
        break

    age = int(input("Enter age: "))
    severity = int(input("Enter severity (1-10): "))

    # Store patient as 2D list row
    patients.append([name, age, severity])

# Print report
print("--- Patient Report ---")

# Loop through patients
i = 0

while i < len(patients):

    name = patients[i][0]
    age = patients[i][1]
    severity = patients[i][2]

    # Decide priority
    if age >= 60 or severity >= 7:

        status = "Priority Treatment"
        priority_count += 1

    elif age >= 18 and severity >= 4:

        status = "Normal Treatment"
        normal_count += 1

    else:

        status = "Standard Queue"
        standard_count += 1

    # Print patient info
    print(f"{name} | Age: {age} | Severity: {severity} -> {status}")

    i += 1

# Final counts
print("Priority Treatment :", priority_count)
print("Normal Treatment :", normal_count)
print("Standard Queue :", standard_count)