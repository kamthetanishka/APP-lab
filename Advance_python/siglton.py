# Singleton Design Pattern
class StudentDatabase:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating Student Database Connection...\n")
            cls._instance = super().__new__(cls)
            cls._instance.students = {}

        return cls._instance

    # Add student
    def add_student(self, roll_no, name):
        self.students[roll_no] = name
        print(f"Student {name} added successfully.")

    # Display all students
    def display_students(self):
        print("\n------ Student Database ------")

        if len(self.students) == 0:
            print("Database is Empty")
        else:
            for roll, name in self.students.items():
                print(f"Roll No : {roll}   Name : {name}")

        print("------------------------------\n")

# Attendance Module
print("Attendance Module")
attendance_db = StudentDatabase()
attendance_db.add_student(101, "Ram")
attendance_db.add_student(102, "Sita")
attendance_db.display_students()

# Examination Module
print("Examination Module")
exam_db = StudentDatabase()
exam_db.display_students()

# Fees Module
print("Fees Module")
fees_db = StudentDatabase()
fees_db.add_student(103, "Radha")
fees_db.display_students()

# Verify Singleton
print("Memory Address Verification")

print("Attendance DB :", id(attendance_db))
print("Exam DB       :", id(exam_db))
print("Fees DB       :", id(fees_db))

print()

print("attendance_db is exam_db :", attendance_db is exam_db)
print("exam_db is fees_db       :", exam_db is fees_db)