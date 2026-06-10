'''
START
   |
   v
Create department list
   |
   v
Create 3D course list
   |
   v
Set successful registrations = 0
   |
   v
Start department while loop
   |
   v
Start course while loop
   |
   v
Get course details
   |
   +--> Check Open/Full
   |
   +--> Print course info
   |
   v
Next course
   |
   v
Next department
   |
   v
Start registration loop
   |
   v
Input department number
   |
   +--> Is input -1?
   |          |
   | YES      v
   |--------> BREAK
   |
   v
Input course number
   |
   v
Check course availability
   |
   +--> Full?
   |        |
   | YES    v
   |    Print failed message
   |
   v
Increase enrolled count
   |
   +--> Increase registration counter
   |
   +--> Print success message
   |
   v
Repeat loop
   |
   v
Print total registrations
   |
   v
END

'''
# Step 1: Store department names
departments = ["Engineering", "Business", "Arts"]


# Step 2: Create 3D list
# courses[department][course][field]

# Field:
# [0] = course name
# [1] = credits
# [2] = max seats
# [3] = enrolled students

courses = [

    [   # Engineering

        ["Algorithms", 3, 30, 28],
        ["Networks", 3, 25, 25],
        ["Databases", 2, 35, 10],
        ["AI Basics", 4, 20, 20]
    ],

    [   # Business

        ["Marketing", 3, 40, 38],
        ["Finance", 3, 30, 30],
        ["Management", 2, 35, 20],
        ["Economics", 4, 25, 25]
    ],

    [   # Arts

        ["History", 3, 30, 15],
        ["Philosophy", 3, 20, 20],
        ["Literature", 2, 25, 10],
        ["Fine Arts", 4, 20, 18]
    ]
]


# Variable to count successful registrations
successful_registrations = 0


print("============================================")
print("UNIVERSITY COURSE CATALOG")
print("============================================")


# --------------------------------------------
# OUTER WHILE LOOP FOR DEPARTMENTS
# --------------------------------------------

d = 0

while d < len(departments):


    # Print department name
    print("Department:", departments[d])


    # --------------------------------------------
    # INNER WHILE LOOP FOR COURSES
    # --------------------------------------------

    c = 0

    while c < len(courses[d]):


        # Get course details
        course_name = courses[d][c][0]

        credits = courses[d][c][1]

        max_seats = courses[d][c][2]

        enrolled = courses[d][c][3]


        # Check course status
        if enrolled < max_seats:

            status = "Open"

        else:

            status = "Full"


        # Print course information
        print(
            f"{c}. {course_name} | "
            f"Credits: {credits} | "
            f"Seats: {max_seats} | "
            f"Enrolled: {enrolled} | "
            f"{status}"
        )


        # Move to next course
        c = c + 1


    # Move to next department
    d = d + 1


# ============================================
# REGISTRATION LOOP
# ============================================

while True:


    # Ask department number
    department_number = int(
        input("Enter department number (0-2, or -1 to exit): ")
    )


    # Exit condition
    if department_number == -1:

        break


    # Ask course number
    course_number = int(
        input("Enter course number (0-3): ")
    )


    # Get max seats
    max_seats = courses[department_number][course_number][2]


    # Get enrolled count
    enrolled = courses[department_number][course_number][3]


    # --------------------------------------------
    # CHECK COURSE AVAILABILITY
    # --------------------------------------------

    if enrolled >= max_seats:

        print("Registration failed: Course is full.")


    else:

        # Increase enrolled count
        courses[department_number][course_number][3] += 1


        # Increase successful registration count
        successful_registrations += 1


        # Get updated enrolled count
        updated_enrolled = courses[department_number][course_number][3]


        # Get course name
        course_name = courses[department_number][course_number][0]


        # Print confirmation
        print(
            f"Registered successfully for {course_name}! "
            f"(Enrolled: {updated_enrolled}/{max_seats})"
        )


# ============================================
# FINAL REPORT
# ============================================

print(
    f"Total successful registrations this session: "
    f"{successful_registrations}"
)