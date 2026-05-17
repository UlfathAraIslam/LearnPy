cgpa = float(input("Enter CGPA:"))

if cgpa >= 3.80:
    print("Full Scholarship") 
elif cgpa >= 3.50:
    print("Half Scholarship")
elif cgpa >= 3.00:
    print("Quarter Scholarship")
else:
    print("No Scholarship")