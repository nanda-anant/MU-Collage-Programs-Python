# 4. Write a program to demonstrate string operations including slicing formatting and built-in string functions. 

text = "Python"

print("Original String:", text)
print("First 6 characters:", text[:6])
print("Last 11 characters:", text[7:])
print("Reverse String:", text[::-1])

name = "Anant"
age = 20
print("\nString Formatting:")
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")

print("\nBuilt-in String Functions:")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))
print("Replace:", text.replace("Python", "Java"))
print("Count of 'm':", text.count("m"))
print("Position of 'Programming':", text.find("Programming"))