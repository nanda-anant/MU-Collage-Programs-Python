# Program to demonstrate constructor and destructor usage

class Student:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Constructor called.")
        print("Student object created.")

    # Method to display student details
    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)

    # Destructor
    def __del__(self):
        print("Destructor called.")
        print("Student object destroyed.")


# Creating an object
student1 = Student("Anant", 22)

# Calling method
student1.display()

# Destructor will be called when the object is deleted
del student1