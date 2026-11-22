
# Program to demonstrate different types of errors and exceptions

print("Demonstration of Errors and Exceptions in Python")

# 1. NameError
try:
    print(x)
except NameError as e:
    print("NameError:", e)

# 2. TypeError
try:
    a = 10 + "Hello"
except TypeError as e:
    print("TypeError:", e)

# 3. ValueError
try:
    num = int("abc")
except ValueError as e:
    print("ValueError:", e)

# 4. ZeroDivisionError
try:
    a = 10 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

# 5. IndexError
try:
    my_list = [10, 20, 30]
    print(my_list[5])
except IndexError as e:
    print("IndexError:", e)

# 6. KeyError
try:
    my_dict = {"name": "Anant", "age": 22}
    print(my_dict["city"])
except KeyError as e:
    print("KeyError:", e)

# 7. FileNotFoundError
try:
    file = open("abc.txt", "r")
except FileNotFoundError as e:
    print("FileNotFoundError:", e)

# 8. Finally Block
finally:
    print("\nProgram execution completed successfully.")
