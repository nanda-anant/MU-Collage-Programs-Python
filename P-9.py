# 9. Write a program to define and use user-defined functions with different types of arguments.

# 1. Function with no arguments
def greet():
    print("Hello, Welcome to Python!")

# 2. Function with positional arguments
def add(a, b):
    print("Addition:", a + b)

# 3. Function with default argument
def welcome(name="Student"):
    print("Welcome", name)

# 4. Function with keyword arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)

greet()
add(10, 20)
welcome()
welcome("Anant")
student(age=20, name="Anant")