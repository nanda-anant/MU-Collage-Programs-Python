# 6. Write a program to illustrate the use of tuples and sets with basic operations.

numbers = (10, 20, 30, 40, 50)
print("Tuple:", numbers)

# Tuple operations
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])
print("Tuple Slicing:", numbers[1:4])
print("Length of Tuple:", len(numbers))

# Creating a set
my_set = {10, 20, 30, 40, 50}
print("\nSet:", my_set)

# Set operations
my_set.add(60)
print("After Adding 60:", my_set)

my_set.remove(20)
print("After Removing 20:", my_set)

# Set union and intersection
set1 = {10, 20, 30}
set2 = {30, 40, 50}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)