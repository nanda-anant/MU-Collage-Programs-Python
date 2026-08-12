# 9. Write a program to demonstrate iterators and iterables in Python. 

numbers = [10, 20, 30, 40, 50]

print("Iterable:", numbers)
iterator = iter(numbers)

print("First Element:", next(iterator))
print("Second Element:", next(iterator))
print("Third Element:", next(iterator))

print("Remaining Elements:")
for value in iterator:
    print(value)