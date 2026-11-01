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


student1 = Student("Abel", 20, "Computer Science")
student2 = Student("Hana", 21, "Accounting")
student3 = Student("Mekdes", 19, "Business")

student1.display_info()
student2.display_info()
student3.display_info()