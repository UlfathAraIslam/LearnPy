#4
'''
-create an empty array to store final list of students
-input name1 and converting to title
-input name2 and converting to title
-input name3 and converting to title
-append name1 to students
-append name2 to students
-append name3 to students
-print the final list of students
-print total students count by using len()
'''

students = []
student_1 = input("Enter name 1:").title()
student_2 = input("Enter name 2:").title()
student_3 = input("Enter name 3:").title()
students.append(student_1)
students.append(student_2)
students.append(student_3)
print("Students:",students)
print("Total students:",len(students))
