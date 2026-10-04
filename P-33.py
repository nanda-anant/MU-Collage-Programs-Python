# Program to demonstrate instance variables and class variables

class Student:

    # Class variable
    college = "Marwadi University"

    # Constructor
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    # Method to display student details
    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("College:", Student.college)


# Creating first object
student1 = Student("Anant", 22)

# Creating second object
student2 = Student("Rahul", 21)

# Displaying details
print("Student 1 Details:")
student1.display()

print("\nStudent 2 Details:")
student2.display()