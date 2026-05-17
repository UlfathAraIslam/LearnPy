age = input("Enter age:")

if age.isdigit():
    age = int(age)
    if age >= 18:
        print("You can watch the movie")
    else:
        print("You cannot watch the movie")
else:
    print("Invalid input")