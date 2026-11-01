class Student:
    school_name = "Akiba Academy"

    def __init__(self, name, age, department, score=None):
        self.name = name
        self.age = age
        self.department = department
        self.score = score

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print()

    def display(self):
        print(f"School: {self.school_name}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Score: {self.score}")
        print()

print("\n","===== Student Score Information =====")

score_student1 = Student("Dawit", 20, "Information Technology", 75)
score_student2 = Student("Liya", 21, "Marketing", 82)
score_student3 = Student("Samuel", 22, "Engineering", 90)

score_student1.display()
score_student2.display()
score_student3.display()

# Update only the first student's score.
score_student1.score = 88

print("After updating Dawit's score:")
score_student1.display()
score_student2.display()
score_student3.display()

# A class attribute belongs to the class and is shared by all objects.
# An instance attribute belongs to one specific object.

# The score is an instance attribute, so each student has an independent
# score. Updating one student's score does not change other students' scores.
