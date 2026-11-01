class Student:

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print()

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print()


student1 = Student("Abel", 20, "Computer Science")
student2 = Student("Hana", 21, "Accounting")
student3 = Student("Mekdes", 19, "Business")

student1.display_info()
student2.display_info()
student3.display_info()