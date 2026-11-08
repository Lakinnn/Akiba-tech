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

    """Answers

What is a class in Python?

  A class is a blueprint that defines the attributes and methods its objects can have.

What is an object?

  An object is a particular instance created from a class. 
  For example, student1 is an object of the Student class.

What is the purpose of __init__()?

__init__() initializes a new object by assigning its starting attributes when the object is created.

What is the difference between an attribute and a method?

  An attribute stores data about an object, such as name. 
  A method is a function defined in a class that describes an action, such as display_info()."""
