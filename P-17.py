#7. Write a program to demonstrate list dictionary and set comprehensions.

numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]

print("List Comprehension:")
print("Squares:", squares)

square_dict = {x: x * x for x in numbers}
print("\nDictionary Comprehension:")
print("Square Dictionary:", square_dict)

even_set = {x for x in numbers if x % 2 == 0}
print("\nSet Comprehension:")
print("Even Numbers:", even_set)