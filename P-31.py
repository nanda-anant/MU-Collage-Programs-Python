# Program to create a class and object in Python

class Student:

    # Method to initialize student details
    def set_data(self, name, age):
        self.name = name
        self.age = age

    # Method to display student details
    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)


# Creating an object of Student class
student1 = Student()

# Taking input from user
name = input("Enter Student Name: ")
age = int(input("Enter Student Age: "))

# Calling methods using object
student1.set_data(name, age)
student1.display()