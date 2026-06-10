#1
'''
START
   |
Create grades list
   |
Create subjects list
   |
Create 3D scores list
   |
Initialize variables
(highest score, fail counter)
   |
Start Grade while loop
   |
Start Subject while loop
   |
Start Student while loop
   |
Get current score
   |
   +------> Add to total
   |
   +------> Print score
   |
   +------> Check highest score
   |
   +------> Check failing score
   |
Next student
   |
Calculate average
   |
Print average
   |
Next subject
   |
Next grade
   |
Print highest score
   |
Print failing students
   |
END

'''
# Step 1: Store grade names
grades = ["Grade 10", "Grade 11"]


# Step 2: Store subject names
subjects = ["Math", "Science", "English"]


# Step 3: Create 3D list
# scores[grade][subject][student]

scores = [

    [   # Grade 10

        [72, 85, 61, 90],   # Math scores
        [55, 48, 79, 83],   # Science scores
        [88, 91, 74, 65]    # English scores
    ],

    [   # Grade 11

        [95, 88, 77, 69],   # Math scores
        [60, 72, 85, 91],   # Science scores
        [45, 78, 83, 90]    # English scores
    ]
]


# Variable to track highest score
highest_score = 0


# Variable to store grade name of highest score
highest_grade = ""


# Variable to store subject name of highest score
highest_subject = ""


# Variable to store student position
highest_student = 0


# Counter for failing students
failing_students = 0


# Print heading
print("========================================")
print("EXAM SCORE REPORT")
print("========================================")

# WHILE LOOP FOR GRADES

g = 0

while g < len(grades):

    # Print current grade name
    print(f"Grade:",grades[g])

    # WHILE LOOP FOR SUBJECTS

    s = 0

    while s < len(subjects):

        # Get current subject scores
        current_subject_scores = scores[g][s]

        # Variable to calculate total
        total = 0

        # Variable to print scores one by one
        st = 0

        # Print subject name
        print(subjects[s], "| Scores:", end=" ")

        # WHILE LOOP FOR STUDENTS

        while st < len(current_subject_scores):

            # Get current student's score
            current_score = current_subject_scores[st]

            # Print score
            print(current_score, end=" ")

            # Add score to total
            total = total + current_score

            # Check highest score
            if current_score > highest_score:

                highest_score = current_score

                highest_grade = grades[g]

                highest_subject = subjects[s]

                highest_student = st + 1


            # Check failing student
            if current_score < 50:

                failing_students = failing_students + 1


            # Move to next student
            st = st + 1


        # Calculate average
        average = total / len(current_subject_scores)


        # Print average rounded to 1 decimal
        print("| Average:", round(average, 1))


        # Move to next subject
        s = s + 1


    # Move to next grade
    g = g + 1


# ========================================
# FINAL REPORT
# ========================================

print("Highest score:", highest_score)

print(
    "Grade:", highest_grade,
    "| Subject:", highest_subject,
    "| Student", highest_student
)

print("Failing students (below 50):", failing_students)