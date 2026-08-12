#7. Write a program to create a dictionary and demonstrate dictionary methods and iteration.

# Creating a dictionary
student = {
    "Name": "Anant",
    "Age": 20,
    "Course": "BCA",
    "City": "Jamnagar"
}

print("Original Dictionary:", student)

# Accessing values
print("Name:", student["Name"])

# Adding a new item
student["College"] = "Marwadi University"
print("After Adding College:", student)

# Updating a value
student["Age"] = 21
print("After Updating Age:", student)

# Dictionary methods
print("\nDictionary Methods:")
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Removing an item
student.pop("City")
print("After Removing City:", student)

# Iteration
print("\nDictionary Iteration:")
for key, value in student.items():
    print(key, ":", value)