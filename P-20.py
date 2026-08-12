#   10.Write a program to generate a sequence of numbers using generator functions and yield keyword. 

def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

num = int(input("Enter the number: "))

print("Generated Sequence:")

for value in generate_numbers(num):
    print(value)