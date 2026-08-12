# 6. Write a program to iterate over lists strings and dictionaries using loops. 

numbers = [10, 20, 30, 40, 50]

print("List Elements:")
for num in numbers:
    print(num)

name = "Python"

print("\nString Characters:")
for ch in name:
    print(ch)

student = {
    "Name": "Anant",
    "Age": 20,
    "Course": "BCA"
}

print("\nDictionary Elements:")
for key, value in student.items():
    print(key, ":", value)