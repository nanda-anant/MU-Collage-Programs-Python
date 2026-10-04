# Program to demonstrate instance, class and static methods

class Student:

    # Class variable
    college = "Marwadi University"

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)

    # Class method
    @classmethod
    def display_college(cls):
        print("College:", cls.college)

    # Static method
    @staticmethod
    def welcome():
        print("Welcome to Python Programming")


# Creating an object
student1 = Student("Anant", 22)

# Calling instance method
print("Instance Method:")
student1.display()

# Calling class method
print("\nClass Method:")
Student.display_college()

# Calling static method
print("\nStatic Method:")
Student.welcome()