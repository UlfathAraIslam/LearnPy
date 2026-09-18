class Student:
    def __init__(self,student_id,name,grade,email=None):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.email = email
    def __str__(self):
        return(f"ID: {self.student_id} | Name: {self.name} | Grade: {self.grade} | Email: {self.email}")
class GradeBook:
    def __init__(self):
        self.students = []
        self.next_id = 1
    # add student
    def add_student(self,name,grade,email=None):
        student = Student(self.next_id, name,grade,email)
        self.students.append(student)
        self.next_id += 1
        print("Student added successfully.")
    # view students
    def view_students(self):
        for student in self.students:
            print(student)
    # search student
    def search_student(self,student_id):
        for student in self.students:
            if student.student_id == student_id:
                print(student)
                return
        print("Student not found.")
    # update grade
    def update_grade(self,student_id,new_grade):
        for student in self.students:
            if student.student_id == student_id:
                student.grade = new_grade
                print("Grade updated successfully.")
                return
        print("Student not found.")
    # delete student
    def delete_student(self,student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student removed successfully.")
                return
        print("Student not found.")
# test
gradebook = GradeBook()
gradebook.add_student("Tanvir", "A", "tanvir@email.com")
gradebook.add_student("Nusrat", "B+")
gradebook.add_student("Rakib", "A-", "rakib@email.com")
gradebook.view_students()
print("\n-- Search --")
gradebook.search_student(2)
print("\n-- Update --")
gradebook.update_grade(3, "A")
print("\n-- Delete --")
gradebook.delete_student(2)
gradebook.view_students()