import os
import sys

# Display current directory
print("Current Directory:", os.getcwd())

# Create a directory
os.mkdir("TestFolder")
print("Directory Created Successfully")

# Create a file inside the directory
file_path = os.path.join("TestFolder", "sample.txt")

with open(file_path, "w") as file:
    file.write("Hello Python")

print("File Created Successfully")

# Display files and directories
print("Directory Contents:", os.listdir())

# Display command line arguments
print("Number of Arguments:", len(sys.argv))
print("Arguments:", sys.argv)

# Remove the file
os.remove(file_path)
print("File Deleted Successfully")

# Remove the directory
os.rmdir("TestFolder")
print("Directory Deleted Successfully")