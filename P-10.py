# 10.Write a program to demonstrate recursion using factorial or Fibonacci series. 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Taking input from user
num = int(input("Enter a number: "))

# Calling recursive function
result = factorial(num)
print("Factorial of", num, "is:", result)