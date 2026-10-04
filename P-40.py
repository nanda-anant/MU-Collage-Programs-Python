# Program to demonstrate file pointer operations
# using seek() and tell() methods

# Create and write data into a file
with open("student.txt", "w") as file:
    file.write("Python Programming")

# Open the file for reading
with open("student.txt", "r") as file:

    # Display initial file pointer position
    print("Initial file pointer position:", file.tell())

    # Read first 6 characters
    data = file.read(6)
    print("Data read:", data)

    # Display current file pointer position
    print("Current file pointer position:", file.tell())

    # Move file pointer to position 0
    file.seek(0)
    print("File pointer after seek(0):", file.tell())

    # Read complete data
    data = file.read()
    print("Data after seek(0):", data)

    # Move file pointer to position 7
    file.seek(7)
    print("File pointer after seek(7):", file.tell())

    # Read remaining data
    data = file.read()
    print("Data after seek(7):", data)