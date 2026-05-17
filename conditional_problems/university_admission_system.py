gpa = float(input("Enter GPA:"))
ielts = float(input("Enter IELTS:"))


if gpa >= 3.5 and ielts >= 6.5:
        print("Eligible for admission")
elif gpa < 3.5:
        print("GPA requirement not met")
elif ielts < 6.5:
        print("IELTS requirement not met")
else:
    print("GPA and IELTS score must be numbers")