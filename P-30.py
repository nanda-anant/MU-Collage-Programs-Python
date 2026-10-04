# Program to extract specific information from a text file
# using regular expressions

import re

# Create a text file and write sample data
with open("data.txt", "w") as file:
    file.write("Name: Anant Nanda\n")
    file.write("Email: anant@gmail.com\n")
    file.write("Phone: 9876543210\n")
    file.write("Contact Email: student@example.com\n")
    file.write("Mobile: 9123456780\n")

# Open and read the text file
with open("data.txt", "r") as file:
    text = file.read()

# Regular expression patterns
email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
phone_pattern = r'\b\d{10}\b'

# Extract email addresses
emails = re.findall(email_pattern, text)

# Extract phone numbers
phone_numbers = re.findall(phone_pattern, text)

# Display extracted information
print("Email Addresses:")
for email in emails:
    print(email)

print("\nPhone Numbers:")
for phone in phone_numbers:
    print(phone)

print("\nInformation extracted successfully.")