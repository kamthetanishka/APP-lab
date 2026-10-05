#1. Student Management System. Develop a Python application to manage student details using Object-Oriented Programming.
#Requirements
#Create a Student class with the following data members:Roll Number, Name, Marks
#Assign Grade based on marks:A (Marks ≥ 90), B (Marks ≥ 75), C (Marks ≥ 60), F (Marks < 60)
#Create a College class.
#Add student objects to the college.
#Display all student details.

class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks
        self.grade = self.assign_grade()

    def assign_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "F"
class College:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        print("\n------ Student Details ------")
        if len(self.students) == 0:
            print("No students in the college.")
        else:
            for student in self.students:
                print(f"Roll Number: {student.roll_number}, Name: {student.name}, Marks: {student.marks}, Grade: {student.grade}")
        print("------------------------------\n")

student1 = Student(10, "Shree", 90)
student2 = Student(30,"Ram",45)
student3 = Student(45,"Sita",67)
college = College()
college.add_student(student1)
college.add_student(student2)
college.add_student(student3)
college.display_students()