#8. Write a program to explain mutable and immutable objects in Python. 

a = 10
print("Original value of a:", a)

a = 20
print("After changing a:", a)

numbers = [10, 20, 30]
print("\nOriginal list:", numbers)

numbers[0] = 100
print("After changing first element:", numbers)

numbers.append(40)
print("After adding an element:", numbers)