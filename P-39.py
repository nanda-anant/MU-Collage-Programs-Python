# Program to read and write data into a file
# using different file modes

# Write mode
file = open("student.txt", "w")
file.write("Name: Anant Nanda\n")
file.write("Course: MCA\n")
file.write("University: Marwadi University\n")
file.close()

print("Data written successfully using write mode.")


# Read mode
file = open("student.txt", "r")
data = file.read()
file.close()

print("\nData read from file:")
print(data)


# Append mode
file = open("student.txt", "a")
file.write("Semester: 1\n")
file.write("Subject: Python Programming\n")
file.close()

print("Data appended successfully using append mode.")


# Read the updated file
file = open("student.txt", "r")
data = file.read()
file.close()

print("\nUpdated file data:")
print(data)