#1. Write a program to create and import a userdefined module. 
import os

# Create a user-defined module
with open("mymodule.py", "w") as file:
    file.write("""
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
""")

# Import the user-defined module
import mymodule

a = 10
b = 5

print("Addition =", mymodule.add(a, b))
print("Multiplication =", mymodule.multiply(a, b))