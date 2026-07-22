age = input("Enter age:")
fare = ""

if age.isdigit():
    age = int(age)

    if age <= 12 :
        fare = 150

    elif age <= 17 :
        fare = 300

    elif age <= 59 :
        fare = 500

    elif age >= 60 :
        fare = 200
    print("Bus fare:",fare, "yen")

else:
    print("Invalid input")