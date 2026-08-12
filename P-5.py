# 5. Write a program to create and manipulate lists using indexing slicing and list comprehensions.

numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)

# Indexing
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# Slicing
print("First Three Elements:", numbers[:3])
print("Last Three Elements:", numbers[2:])

# Add an element
numbers.append(60)
print("After Append:", numbers)

# Remove an element
numbers.remove(20)
print("After Remove:", numbers)

# List Comprehension
squares = [x * x for x in numbers]
print("Squares using List Comprehension:", squares)

# List comprehension with condition
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even Numbers:", even_numbers)