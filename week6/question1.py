class Student:
    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department

    def display_info(self):
        print(
            f"Name: {self.name}, "
            f"Student ID: {self.student_id}, "
            f"Department: {self.department}"
        )

    def introduce(self):
        print(
            f"Hello, my name is {self.name}. "
            f"I study {self.department}."
        )


student1 = Student("Abel", "S1001", "Computer Science")
student2 = Student("Hana", "S1002", "Accounting")
student3 = Student("Dawit", "S1003", "Engineering")

for student in (student1, student2, student3):
    student.display_info()
    student.introduce()
    print()
