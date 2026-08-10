age = int(input("Enter your age: "))
if 0<= age<12:
    print("Child")
elif 12<= age <= 22:
    print("Student")
elif 23<=age<=64:
    print("Adult")
elif age>=65:
    print("Senior")
else:
    print("Wrong Input")