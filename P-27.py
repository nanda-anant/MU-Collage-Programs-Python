import shutil
import os

# Create a sample file
with open("sample.txt", "w") as file:
    file.write("Hello Python")

# Copy the file
shutil.copy("sample.txt", "copy.txt")
print("File copied successfully")

# Move the copied file
shutil.move("copy.txt", "moved.txt")
print("File moved successfully")

# Delete the moved file
os.remove("moved.txt")
print("File deleted successfully")

# Delete the original file
os.remove("sample.txt")
print("Original file deleted successfully")